import pandas as pd

# drop_columns,keep_columns = ["list","of","String"]
def drop_columns(df,drop_columns=None,keep_columns=None):
    if keep_columns:
        drop_columns = []
        for col,_ in df.iteritems():
            if col not in keep_columns and col not in drop_columns:
                drop_columns.append(col)
    df.drop(columns=drop_columns,inplace=True)
    return df
    
def cut_data(df,argv=[]):
    for i in (argv):
        i = i.split("=")
        try:
            if len(i) != 2:
                raise Exception
            if i[0].startswith("colu"):
                columns = i[1].split(",")
                df = drop_columns(df,keep_columns=columns)
            else:            
                params = i[1].split(",")
                if len(params) > 1:
                    df = df[(df[i[0]] >= float(params[0])) & (df[i[0]] <= float(params[1]))]
                else:
                    try:
                        df = df[df[i[0]] == float(params[0])]
                    except:
                        df = df[df[i[0]] == (params[0])]

        except:
            print("Error Trimming " , i[0],params)
    return df



def cut_rows(df,columnName,targetValue):
    df = df[(df != targetValue).all(1)]
    return df
