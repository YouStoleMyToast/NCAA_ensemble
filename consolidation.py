#!/usr/bin/env python3

import pandas as pd
import refine, display
import batch_handler as batch
import sklearn
import pandas as pd
import numpy as np

results_df = batch.get_data("stage1/MNCAATourneyCompactResults.csv")
seeds_df = batch.get_data("stage1/MNCAATourneySeeds.csv")




"""
losing seed is seed 2

"""


def get_winning_seed():

    winning_seed = pd.merge(results_df,seeds_df,left_on=["Season","WTeamID"],right_on=["Season","TeamID"])
    winning_seed = winning_seed.drop(["TeamID"],axis=1)
    winning_seed = winning_seed.rename(mapper={"Seed": "Seed1", "WTeamID": "TeamID1"},axis=1)
    winning_seed["Result"] = 1
    
    winning_seed = pd.merge(winning_seed,seeds_df,left_on=["Season","LTeamID"],right_on=["Season","TeamID"])
    winning_seed = winning_seed.drop(["TeamID"],axis=1)
    winning_seed = winning_seed.rename(mapper={"Seed": "Seed2", "LTeamID": "TeamID2"},axis=1)
    winning_seed = winning_seed.drop(["DayNum","WScore","LScore","WLoc","NumOT"],axis=1)
    #print(winning_seed)
    return winning_seed
    
def get_losing_seed():
    losing_seed = pd.merge(results_df,seeds_df,left_on=["Season","LTeamID"],right_on=["Season","TeamID"])
    losing_seed = losing_seed.drop(["TeamID"],axis=1)
    losing_seed = losing_seed.rename(mapper={"Seed": "Seed1", "LTeamID": "TeamID1"},axis=1)
    losing_seed["Result"] = 0
    
    losing_seed = pd.merge(losing_seed,seeds_df,left_on=["Season","WTeamID"],right_on=["Season","TeamID"])
    losing_seed = losing_seed.drop(["TeamID"],axis=1)
    losing_seed = losing_seed.rename(mapper={"Seed": "Seed2", "WTeamID": "TeamID2"},axis=1)
    losing_seed = losing_seed.drop(["DayNum","WScore","LScore","WLoc","NumOT"],axis=1)
    #print(losing_seed)
    return losing_seed







'''  /////////////////////////////////
    ACTUAL CONSOLIDATION HAPPENS BELOW
    /////////////////////////////////
'''




def get_all_seed():
    #TeamID1 Is Winning Seed
    results_df = batch.get_data("stage1/MNCAATourneyCompactResults.csv")
    seeds_df = batch.get_data("stage1/MNCAATourneySeeds.csv")

    winning_seed = get_winning_seed()
    losing_seed = get_losing_seed()

    all_seed = pd.concat([winning_seed,losing_seed],sort=True)
    #all_seed.to_csv("./data/seed_data-consolidated.csv",index=False)
    return all_seed


    
def get_seed_compact_results():
    all_seed = get_all_seed()
    tourney_compact_data = batch.get_data("stage1/MNCAATourneyCompactResults.csv")
    all_seed = all_seed.rename(mapper={"TeamID1":"WTeamID","TeamID2":"LTeamID"},axis=1)
    #tourney_compact_data = tourney_compact_data.drop(["Season"],axis=1)
    seed_compact = pd.merge(tourney_compact_data,all_seed,left_on=["Season","WTeamID","LTeamID"],right_on=["Season","WTeamID","LTeamID"])

    seed_compact = seed_compact.rename(mapper={"Seed1":"WSeed","Seed2":"LSeed"},axis=1)
    #print(seed_compact)
    return seed_compact

def get_seed_detailed_results():
    all_seed = get_all_seed()
    tourney_detailed_data = batch.get_data("stage1/MNCAATourneyDetailedResults.csv")
    all_seed = all_seed.rename(mapper={"TeamID1":"WTeamID","TeamID2":"LTeamID"},axis=1)
    #tourney_compact_data = tourney_compact_data.drop(["Season"],axis=1)
    seed_detailed = pd.merge(tourney_detailed_data,all_seed,left_on=["Season","WTeamID","LTeamID"],right_on=["Season","WTeamID","LTeamID"])

    seed_detailed = seed_detailed.rename(mapper={"Seed1":"WSeed","Seed2":"LSeed"},axis=1)
    #print(seed_detailed)
    seed_detailed = seed_detailed.drop(["Result"],axis=1)
    return seed_detailed

def get_detail_seed_season():
    seasons = batch.get_data("stage1/MSeasons.csv")
    seed_details = get_seed_detailed_results()
    detail_seed_season = pd.merge(seasons,seed_details,left_on=["Season"],right_on=["Season"])
    #print(detail_seed_season)
    detail_seed_season = detail_seed_season.drop(["DayZero"],axis=1)
    return detail_seed_season

def get_season_slots():
    slot_data = batch.get_data("stage1/MNCAATourneySlots.csv")
    seasons = batch.get_data("stage1/MSeasons.csv")
    #print(slot_data)
    slot_season = pd.merge(slot_data,seasons,left_on=["Season"],right_on=["Season"])
    slot_season = slot_season.drop(["DayZero"],axis=1)
    #print(slot_season)
    return slot_season


def get_player_detail_seed_season_win(): #Players id matched with winning team
    player_data = batch.get_data("stage1/MPlayers.csv")
    detail_seed_season_data = get_detail_seed_season()
    #print(player_data)
    detail_seed_player_season_data = pd.merge(player_data,detail_seed_season_data,left_on=["TeamID"],right_on=["WTeamID"])
    #print(detail_seed_player_season_data)
    return detail_seed_player_season_data
def get_player_detail_seed_season_loss(): #Players id matched with winning team
    player_data = batch.get_data("stage1/MPlayers.csv")
    detail_seed_season_data = get_detail_seed_season()
    #print(player_data)
    detail_seed_player_season_data = pd.merge(player_data,detail_seed_season_data,left_on=["TeamID"],right_on=["LTeamID"])
    #print(detail_seed_player_season_data)
    return detail_seed_player_season_data
    
def get_player_wins_losses(write=False): #This returns the players df with total number of each player wins in the tourney
    myDataWin = get_player_detail_seed_season_win()
    winData = []
    playerIDs = myDataWin.PlayerID.unique()
    for playerid in playerIDs:
        total_wins = myDataWin["PlayerID"].value_counts()[playerid]
        winData.append({"PlayerID":playerid,\
                     "player_total_wins":total_wins,\
        })

    winners_df = (pd.DataFrame(winData))

    myDataLoss = get_player_detail_seed_season_loss()
    
    lossData = []
    playerIDs = myDataLoss.PlayerID.unique()
    for playerid in playerIDs:
        total_losses = myDataLoss["PlayerID"].value_counts()[playerid]
        lossData.append({"PlayerID":playerid,\
                     "player_total_losses":total_losses,\
        })

    losers_df = pd.DataFrame(lossData)
    count_df = pd.merge(winners_df,losers_df,left_on=["PlayerID"],right_on=["PlayerID"])
    
    player_data = batch.get_data("stage1/MPlayers.csv")
    player_data = pd.merge(player_data,count_df,left_on=["PlayerID"],right_on=["PlayerID"])

    if write:
        player_data.to_csv("./data/derived/MPlayers.csv",index=False)
    return player_data




def get_team_win_loss_data(write=False):
    player_data = get_player_wins_losses(write)

    team_data = batch.get_data("stage1/MTeamConferences.csv")

    #These are teams ids from the player object
    team_ids = player_data.TeamID.unique()
    #Drop The Teams That Have No Wins or Losses In The Tourney
    team_data = team_data[team_data["TeamID"].isin(team_ids)]

    visited = []
    data = []
    for team_id in team_ids:
        if team_id in visited:
            continue
        visited.append(team_id)
        team_players = player_data[player_data["TeamID"] == team_id]
        wins_stat = team_players["player_total_wins"].iloc[0]
        losses_stat = team_players["player_total_losses"].iloc[0]
        data.append({"TeamID":team_id,\
                     "tourney_game_wins":wins_stat,\
                     "tourney_game_losses":losses_stat\
        })
    team_win_loss_data = pd.DataFrame(data)

    team_win_loss_data = pd.merge(team_data,team_win_loss_data,left_on=["TeamID","Season"],right_on=["TeamID","Season"])


    
    if write:
        team_win_loss_data.to_csv("./data/derived/MTeams.csv",index=False)

    return team_win_loss_data


def derive_team_data(write=False):
    team_data = batch.get_data("derived/MTeams.csv")
    slot_data = batch.get_data("stage1/MNCAATourneySlots.csv")
    seed_data = get_seed_detailed_results()
    
    print(slot_data)
    print(seed_data)
    print(team_data)
    
    team_seeds = []
    teams = team_data["TeamID"].unique()
    for nTeam in teams:
        team = seed_data[seed_data["WTeamID"] == nTeam]
        team_seed = team.WSeed.iloc[0]
        team_seeds.append({"TeamID":nTeam,\
                           "Seed":team_seed,})
    team_seeds = pd.DataFrame(team_seeds)
    team_data = pd.merge(team_data,team_seeds,left_on="TeamID",right_on="TeamID")
    team_data.sort_values("Season",axis=0,ascending=True)
    print(team_data)
        

    
    return
