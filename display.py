import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt



###cols = ["list","of","Strings"]
def pairplot(df,cols="aLL"):
    if cols == "aLL":
        sns.pairplot(df)
    else:
        sns.pairplot(df,vars=cols)
    plt.show()
    return



### columns = ["x-axis/y-axis","x-axis/y-axis"]
def bar(df,columns):
    plt.figure(figsize=(6,4))
    base_size = ((len(columns )%  3) * 100 + 11) + (len(columns) // 3)
    for i in range(len(columns)):
        plt.subplot(base_size + i)
        cols = columns[i].split("/")
        plt.bar(df[cols[0]],df[cols[1]])
        plt.xlabel(cols[0])
        plt.ylabel(cols[1])
    plt.show()

def scatter(df,columns):
    plt.figure(figsize=(6,4))
    base_size = (((len(columns ) % 4) +1) * 100 + 11) + (len(columns) // 3)
    for i in range(len(columns)):
        plt.subplot(base_size + i)
        cols = columns[i].split("/")
        plt.scatter(df[cols[0]],df[cols[1]])
        plt.xlabel(cols[0])
        plt.ylabel(cols[1])
    plt.show()

    
    
    
    