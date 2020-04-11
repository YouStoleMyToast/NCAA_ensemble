import refine, display
import batch_handler as batch
import sklearn
import pandas as pd
import numpy as np
import consolidation


def load_top_level_files():
    players = batch.get_data("MPlayers.csv")
    print(players)
    events15 = batch.get_data("MEvents2015.csv")
    #events16 = batch.get_data("MEvents2016.csv")
    #events17 = batch.get_data("MEvents2017.csv")
    #events18 = batch.get_data("MEvents2018.csv")
    #events19 = batch.get_data("MEvents2019.csv")
    print(events15)


def load_stage1_files():
    cities = batch.get_data("stage1/Cities.csv")
    print(cities)
    conferences = batch.get_data("stage1/Conferences.csv")
    print(conferences)
    conference_tourney_games = batch.get_data("stage1/MConferenceTourneyGames.csv")
    print(conference_tourney_games)
    seasons = batch.get_data("stage1/MSeasons.csv")
    print(seasons)
    tourney_compact_results = batch.get_data("stage1/MNCAATourneyCompactResults.csv")
    print(tourney_compact_results)
    tourney_detailed_results = batch.get_data("stage1/MNCAATourneyDetailedResults.csv")
    print(tourney_detailed_results)
    season_compact_results = batch.get_data("stage1/MRegularSeasonCompactResults.csv")
    print(season_compact_results)
    season_detailed_results = batch.get_data("stage1/MRegularSeasonDetailedResults.csv")
    print(season_detailed_results)
    ordinals = batch.get_data("stage1/MMasseyOrdinals.csv")
    print(ordinals)
    seeds = batch.get_data("stage1/MNCAATourneySeeds.csv")
    print(seeds)
    seed_round_slots = batch.get_data("stage1/MNCAATourneySeedRoundSlots.csv")
    print(seed_round_slots)


def show_seasons():
    seasons = batch.get_data("stage1/MSeasons.csv")
    print("<--------------- SEASONS --------------->")
    print(seasons)
    print("<---------------- SEASON SEED DETAILS -------------->")
    print(consolidation.get_detail_seed_season())
    return
    
def show_compact_results():
    season_compact_results = batch.get_data("stage1/MRegularSeasonCompactResults.csv")
    print("<---------------- SEASON_COMPACT_RESULTS -------------->")
    print(season_compact_results)
    tourney_compact_results = batch.get_data("stage1/MNCAATourneyCompactResults.csv")
    print("<---------------- TOURNEY_COMPACT_RESULTS -------------->")
    print(tourney_compact_results)


def show_winning_seed():
    print("<--------------- Winning Seed --------------->")
    print(consolidation.get_winning_seed())

def show_losing_seed():
    print("<--------------- Losing Seed --------------->")
    print(consolidation.get_losing_seed())

def show_seed_data():
    all_seed = consolidation.get_all_seed()
    print("<-------------------- ALL SEED -------------------->")
    print(all_seed)
    print("<-------------------- COMPACT SEED -------------------->")
    print(consolidation.get_seed_compact_results())
    print("<-------------------- DETAILED SEED -------------------->")
    print(consolidation.get_seed_detailed_results())


def show_team_data():
    print("<----------- TEAM DATA ---------->")
    team_data =  batch.get_data("stage1/MTeams.csv")
    print(team_data)

    
    
def show_conference_tourney_games():
    conference_tourney_games = batch.get_data("stage1/MConferenceTourneyGames.csv")
    print("<-------------- CONFERENCE GAMES ---------------->")
    print(conference_tourney_games)


def show_slot_data():
    slot_data = batch.get_data("stage1/MNCAATourneySlots.csv")
    print("<--------------- SLOTS --------------->")
    print(slot_data)
    print("<--------------- SEASON SLOTS --------------->")
    print(consolidation.get_season_slots())


def show_most_recent_development():
    print("<------------------- SEASON DATA WITH SLOT DATA --------------------->")
    print(consolidation.get_season_slots())
    print("<------------------ DETAIL SEED SEASON DATA WITH PLAYERS  ---------------------->")
    print(consolidation.get_player_detail_seed_season())




'''
I Realized With The Data We Have It Can Be Hard To Find Out How Many Players Have Wins And Losses Individually
The Data We Have Will Assign All Players On The Same Team The Same Number Of Wins And Losses


'''
def development():
    team_data = batch.get_data("stage1/MTeams.csv")
    print(team_data)
    seed_data = consolidation.get_seed_detailed_results()
    print(seed_data)
    combo_win = pd.merge(team_data,seed_data,left_on=["TeamID"],right_on=["WTeamID"])
    combo_loss = pd.merge(team_data,seed_data,left_on=["TeamID"],right_on=["LTeamID"])
    print(combo_win)
    print(combo_loss)
    wins = []
    for index,row in combo_win.iterrows():
        wins.append(1)
    combo_win["result"] = wins
    losses = []
    for index,row in combo_loss.iterrows():
        losses.append(0)
    combo_loss["result"] = losses

    combo = pd.concat([combo_win,combo_loss])
    combo.to_csv("./data/master.csv",index=0)

    return

    
def main():
    development()
    #show_slot_data()
    #show_seasons()
    return


if __name__ == "__main__":
    main()
