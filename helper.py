import pandas as pd
def fetch_team_player(df,team,player):  
    if(team=="All Teams" and player=="All Players"):
        batsman_career=df.groupby('batsman').sum()['batsman_runs'].sort_values(ascending=False).reset_index()
        batsman_career.columns=['Batsman Name','Total Runs Scored']
        batsman_name_game=df[['id','batsman']]
        batsman_name_game.drop_duplicates(inplace=True)
        matches_played_batsman=batsman_name_game['batsman'].value_counts().reset_index().rename(columns={"batsman": "Batsman Name", 'count': "No of matches Played"})
        temp_df=batsman_career
        temp_match=matches_played_batsman
          
    if(team=="All Teams" and player!="All Players"):
        batsman_career_per_team=df.groupby(['batsman','batting_team']).sum()['batsman_runs'].sort_values(ascending=False).reset_index()
        batsman_career_per_team.columns=['Batsman Name','Team','Total Runs Scored for a Team']
        batsman_name_game_per_team=df[['id','batsman','batting_team']]
        batsman_name_game_per_team.drop_duplicates(inplace=True)                                                                                                
        batsman_name_game_per_team = batsman_name_game_per_team[['batsman','batting_team']].value_counts().reset_index().rename(columns={"batsman": "Batsman Name", 'count': "No of matches Played",'batting_team':"Team"})
        temp_df=batsman_career_per_team[batsman_career_per_team['Batsman Name']==player]
        temp_match=batsman_name_game_per_team[batsman_name_game_per_team['Batsman Name']==player]
                                                                                                                                                                               
    if(team!="All Teams" and player=="All Players"):
        batsman_career_per_team=df.groupby(['batsman','batting_team']).sum()['batsman_runs'].sort_values(ascending=False).reset_index()
        batsman_career_per_team.columns=['Batsman Name','Team','Total Runs Scored for a Team']
        batsman_name_game_per_team=df[['id','batsman','batting_team']]
        batsman_name_game_per_team.drop_duplicates(inplace=True)                                                                                                
        batsman_name_game_per_team = batsman_name_game_per_team[['batsman','batting_team']].value_counts().reset_index().rename(columns={"batsman": "Batsman Name", 'count': "No of matches Played",'batting_team':"Team"})
        temp_df=batsman_career_per_team[batsman_career_per_team['Team']==team]
        temp_match=batsman_name_game_per_team[batsman_name_game_per_team['Team']==team]
        
    if(team!="All Teams" and player!="All Players"):
        batsman_career_per_team=df.groupby(['batsman','batting_team']).sum()['batsman_runs'].sort_values(ascending=False).reset_index()
        batsman_career_per_team.columns=['Batsman Name','Team','Total Runs Scored for a Team']
        batsman_name_game_per_team=df[['id','batsman','batting_team']]
        batsman_name_game_per_team.drop_duplicates(inplace=True)                                                                                                
        batsman_name_game_per_team = batsman_name_game_per_team[['batsman','batting_team']].value_counts().reset_index().rename(columns={"batsman": "Batsman Name", 'count': "No of matches Played",'batting_team':"Team"})
        temp_df=batsman_career_per_team[(batsman_career_per_team['Team']==team) & (batsman_career_per_team['Batsman Name']==player)]
        temp_match=batsman_name_game_per_team[(batsman_name_game_per_team['Batsman Name']==player) & (batsman_name_game_per_team['Team']==team) ]  
                                                                                                        
    return temp_df.head(40),temp_match.head(40)                                                                                                  

def team_batsman_list(df):
    teams=df['batting_team'].unique().tolist()
    teams.insert(0,'All Teams')

    player=df['batsman'].unique().tolist()
    player.insert(0,'All Players')
    return teams,player
def get_bowler(df):
    bowler_list=df['bowler'].unique().tolist()
    bowler_list.insert(0,'All Bowler')
    return bowler_list

def get_fielder(df):
    df['fielder']=df['fielder'].str.rstrip(' (sub)')
    fielder=df['fielder'][df['dismissal_kind']=='caught'].unique().tolist()
    fielder.insert(0,'All Fielder')
    return fielder

def fetch_team_bowler(df,team,player):
    excluded_dismissal=['run out','obstructing the field','retired hurt'] #Since these doesnt come into bowlers account
    
    if(team=="All Teams" and player=="All Bowler"):
        bowler_career=df[~df['dismissal_kind'].isin(excluded_dismissal)].groupby('bowler').sum()['is_wicket'].sort_values(ascending=False).reset_index()
        bowler_career.columns=['Bowler Name','Total Wickets']
        bowler_name_game=df[['id','bowler']]
        bowler_name_game.drop_duplicates(inplace=True)
        temp_match=bowler_name_game['bowler'].value_counts().reset_index().rename(columns={'bowler':'Bowler Name','count': "No of matches played"})
        temp_df=bowler_career
            
    elif(team=="All Teams" and player!="All Bowler"):
        bowler_career_per_team=df[~df['dismissal_kind'].isin(excluded_dismissal)].groupby(['bowler','bowling_team']).sum()['is_wicket'].sort_values(ascending=False).reset_index()
        bowler_career_per_team.columns=['Bowler Name','Team','Total Wickets']
        bowler_name_game_per_team=df[['id','bowler','bowling_team']]
        bowler_name_game_per_team.drop_duplicates(inplace=True)                                                                                                
        temp=bowler_name_game_per_team[['bowler','bowling_team']].value_counts().reset_index().rename(columns={'bowler':'Bowler Name','bowling_team':'Team','count':"No of matches bowled"})
        temp_df=bowler_career_per_team[bowler_career_per_team['Bowler Name']==player]
        temp_match=temp[temp['Bowler Name']==player]
                                                                                                             
    elif(team!="All Teams" and player=="All Bowler"):
        bowler_career_per_team=df[~df['dismissal_kind'].isin(excluded_dismissal)].groupby(['bowler','bowling_team']).sum()['is_wicket'].sort_values(ascending=False).reset_index()
        bowler_career_per_team.columns=['Bowler Name','Team','Total Wickets']
        bowler_name_game_per_team=df[['id','bowler','bowling_team']]
        bowler_name_game_per_team.drop_duplicates(inplace=True)                                                                                                
        temp=bowler_name_game_per_team[['bowler','bowling_team']].value_counts().reset_index().rename(columns={'bowler':'Bowler Name','bowling_team':'Team','count':"No of matches bowled"})
        temp_df=bowler_career_per_team[bowler_career_per_team['Team']==team]
        temp_match=temp[temp['Team']==team]
        
    elif(team!="All Teams" and player!="All Bowler"):
        bowler_career_per_team=df[~df['dismissal_kind'].isin(excluded_dismissal)].groupby(['bowler','bowling_team']).sum()['is_wicket'].sort_values(ascending=False).reset_index()
        bowler_career_per_team.columns=['Bowler Name','Team','Total Wickets']
        bowler_name_game_per_team=df[['id','bowler','bowling_team']]
        bowler_name_game_per_team.drop_duplicates(inplace=True)                                                                                                
        temp=bowler_name_game_per_team[['bowler','bowling_team']].value_counts().reset_index().rename(columns={'bowler':'Bowler Name','bowling_team':'Team','count':"No of matches bowled"})
        temp_df=bowler_career_per_team[(bowler_career_per_team['Team']==team) & (bowler_career_per_team['Bowler Name']==player)]
        temp_match=temp[(temp['Team']==team) & (temp['Bowler Name']==player)]
                                                                                                        
    return temp_df.head(40),temp_match.head(40)   


def fetch_catches(df,fielder):
    df['fielder']=df['fielder'].str.rstrip(' (sub)')
    catches=df['fielder'][df['dismissal_kind']=='caught'].value_counts()
    catches=catches.reset_index()
    catches.columns=['Fielder Name','No of catches']
    if(fielder!='All Fielder'):
        catches=catches[catches['Fielder Name']==fielder]
    
    return catches.head(40)
    
def fetch_runout(df,fielder):
    df['fielder']=df['fielder'].str.rstrip(' (sub)')
    runouts=df['fielder'][df['dismissal_kind']=='run out'].value_counts()
    runouts=runouts.reset_index()
    runouts.columns=['Fielder Name','No of Run outs']
    if(fielder!='All Fielder'):
        runouts=runouts[runouts['Fielder Name']==fielder]
    
    return runouts.head(40)

def fetch_stumping(df,fielder):
    df['fielder']=df['fielder'].str.rstrip(' (sub)')
    stumping=df['fielder'][df['dismissal_kind']=='stumped'].value_counts()
    stumping=stumping.reset_index()
    stumping.columns=['Fielder Name','No of Stumping']
    if(fielder!='All Fielder'):
        stumping=stumping[stumping['Fielder Name']==fielder]

    return stumping.head(40)  


def team_table(df):
    runs_scored_per_team=df.groupby('batting_team').sum()['total_runs'].sort_values(ascending=False).reset_index()
    runs_conceded_per_team=df.groupby('bowling_team').sum()['total_runs'].sort_values(ascending=False).reset_index()
    final=pd.merge(runs_scored_per_team,runs_conceded_per_team,left_on='batting_team',right_on='bowling_team')
    final.drop(columns='bowling_team',inplace=True)
    final.rename(columns={'batting_team':'Team','total_runs_x':'Runs Scored','total_runs_y':'Runs Conceded'},inplace=True)
    temp=df[['id','batting_team']]
    temp.drop_duplicates(inplace=True)
    matches_per_team=temp['batting_team'].value_counts().reset_index().rename(columns={'index':'Team','batting_team':'No of matches Played'})
    final=pd.merge(final,matches_per_team,on='Team')
    final['Runs Scored Per Match']=final['Runs Scored']/final['No of matches Played']
    final['Runs Conceded Per Match']=final['Runs Conceded']/final['No of matches Played']
    final['Runs Scored Per Match']=final['Runs Scored Per Match'].astype(int)
    final['Runs Conceded Per Match']=final['Runs Conceded Per Match'].astype(int)
    return final


def team_table_wicket(df):
    wicket_losen_per_team=df.groupby('batting_team').sum()['is_wicket'].sort_values(ascending=False).reset_index().rename(columns={'batting_team':"Team"})
    wicket_taken_per_team=df.groupby('bowling_team').sum()['is_wicket'].sort_values(ascending=False).reset_index().rename(columns={'bowling_team':"Team"})
    final=pd.merge(wicket_taken_per_team,wicket_losen_per_team,on='Team')
    final.rename(columns={'is_wicket_x':'Wicket Taken','is_wicket_y':'Wicket Losen'},inplace=True)
    temp=df[['id','batting_team']]
    temp.drop_duplicates(inplace=True)
    matches_per_team=temp['batting_team'].value_counts().reset_index().rename(columns={'index':'Team','batting_team':'No of matches Played'})
    final=pd.merge(matches_per_team,final,on='Team')
    final['Wicket Taken Per Match']=final['Wicket Taken']/final['No of matches Played']
    final['Wicket Losen Per Match']=final['Wicket Losen']/final['No of matches Played']
    final['Wicket Taken Per Match']=final['Wicket Taken Per Match'].astype(int)
    final['Wicket Losen Per Match']=final['Wicket Losen Per Match'].astype(int)
    return final

def sixes_hit(df):
    temp=df[(df['batsman_runs']==6) & (df['extra_runs']==0) & (df['non_boundary']==0)]
    no_of_six_hitted=temp['batting_team'].value_counts().reset_index().rename(columns={'index':'Teams','batting_team':'No of Sixes Hitted'})
    return no_of_six_hitted

def sixes_conced(df):
    temp=df[(df['batsman_runs']==6) & (df['extra_runs']==0) & (df['non_boundary']==0)]
    no_of_six_conceded=temp['bowling_team'].value_counts().reset_index().rename(columns={'index':'Teams','bowling_team':'No of Sixes Conceded'})
    return no_of_six_conceded

def four_hit(df):
    temp=df[(df['batsman_runs']==4) & (df['extra_runs']==0) & (df['non_boundary']==0)]
    no_of_four_hitted=temp['batting_team'].value_counts().reset_index().rename(columns={'index':'Teams','batting_team':'No of Fours Hitted'})
    return no_of_four_hitted

def four_conced(df):
    temp=df[(df['batsman_runs']==4) & (df['extra_runs']==0) & (df['non_boundary']==0)]
    no_of_four_conceded=temp['bowling_team'].value_counts().reset_index().rename(columns={'index':'Teams','bowling_team':'No of Fours Conceded'})
    return no_of_four_conceded














