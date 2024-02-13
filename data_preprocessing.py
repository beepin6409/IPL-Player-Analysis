import pandas as pd

def preprocessor(df):
    df.loc[df['batting_team']=='Rising Pune Supergiants','batting_team']='Rising Pune Supergiant'
    df.loc[df['batting_team']=='Delhi Daredevils','batting_team']='Delhi Capitals'
    df.loc[df['bowling_team']=='Rising Pune Supergiants','bowling_team']='Rising Pune Supergiant'
    df.loc[df['bowling_team']=='Delhi Daredevils','bowling_team']='Delhi Capitals'
    df.drop_duplicates(inplace=True)
    return df
