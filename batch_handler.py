import pandas as pd
from sklearn.model_selection import train_test_split
import os,sys



def get_data(filename,fillna=False):
    try:
        df = pd.read_csv("./data/"+filename)
    except:
        df = pd.read_excel("./data/"+filename)
    return df









def split_train_test(df,test_size=.2):
    train_data,test_data = train_test_split(df,test_size = test_size,random_state=9)
    return train_data,test_data

def write_test(df,fout="./data_center/test_data.csv"):
    try:
        df.to_csv(fout)
    except:
        print("Error Writing Test Data to File")

def write_training(df,fout="./data_center/training_data.csv"):
    try:
        df.to_csv(fout)
    except:
        print("Error Writing Training Data to File")

def load_test(fin="./data_center/test_data.csv"):
    try:
        df = pd.read_csv(fin)
    except:
        print("Error Reading From Specified File Setting to Default")
        df = pd.read_csv("./data_center/test_data.csv")
    return df


def load_training(fin="./data_center/training_data.csv"):
    try:
        df = pd.read_csv(fin)
    except:
        print("Error Reading From Specified File Setting to Default")
        df = pd.read_csv("./training_data.csv")
    return df

def get_minibatch(df,start=0,size=.1):
    return_size = len(df) * size
    return df[start * return_size:(start * return_size) + round(return_size)]


def main(argv):
    if len(argv) > 1:
        filename = argv[1]

    df = pd.read_csv(filename,index_col=0)
    train_data,test_data = split_train_test(df)
    write_training(train_data)
    write_test(test_data)
    return

if __name__ == "__main__":
    main(sys.argv)
