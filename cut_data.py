import refine, display
import batch_handler as batch
import process_data
import sklearn
import pandas as pd
import numpy as np
# import consolidation
import random


def cut_preprocessed_data():
    data = batch.get_data("master.csv")
    result_ids = []
    for index,row in data.iterrows():
        team_1 = row["WTeamID"]
        team_2 = row["LTeamID"]
        season = row["Season"]
        ied = str(season) + "_" + str(team_1) + "_" + str(team_2)
        result_ids.append(ied)


    data["result_id"] = result_ids

    print(data)

    predict_season = data[data.Season == 2019]
    historical_data = data[data.Season < 2019]
    print(predict_season)
    print(historical_data)
    print(historical_data.info())
    predict_season.to_csv("data/test.csv")
    historical_data.to_csv("data/train.csv")


    return



def get_column_accuracy(myData,column):
    high_prob = myData[0:int(len(myData)/2)]
    high_probs = len(high_prob[high_prob[column] > .5])


    low_prob = myData[int(len(myData)/2):]
    low_probs = len(low_prob[low_prob[column] < .5])


    
    score = high_probs + low_probs
    return score




def cut_result_data(score):
    score = str(score).split(".")[1]
    data = process_data.get_data("data/test_result.csv")
    # greatest = []
    # for index,row in data.iterrows():
    #     if row[0] > row[1]:
    #         greatest.append(row[0])
    #     else:
    #         greatest.append(row[1])
    # data["Probability"] = greatest
    try:
        zero_score = get_column_accuracy(data,"0")
        one_score = get_column_accuracy(data,"1")

        print("Zero Column Score => \t",zero_score)
        print("One Column Score => \t",one_score)


        if zero_score > one_score:
            myData = {"id":data["result_id"].to_list(),\
                    "Probability":data["0"].to_list(),\
                    }
            myData = pd.DataFrame(myData)
        else:
            myData = {"id":data["result_id"].to_list(),\
                        "Probability":data["1"].to_list(),\
                    }
            myData = pd.DataFrame(myData)
    except:
        myData = {"id":data["result_id"].to_list(),\
                    "Probability":data["0"].to_list(),\
                    }
        myData = pd.DataFrame(myData)


    print(myData)
    myData.to_csv("data/test_results_"+score+".csv",index=0)
    return

def main():
    cut_preprocessed_data()

if __name__ == "__main__":
    main()