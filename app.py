import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import data_preprocessing
import helper


df=pd.read_csv('IPL Ball-by-Ball 2008-2020.csv')
df=data_preprocessing.preprocessor(df)

image=Image.open('ipl_blue.png')



st.sidebar.image(image,width=250)
st.sidebar.title("IPL Player Analysis Website")


user_choice =st.sidebar.radio(
    'Select an option',
    ('Overall Analysis','Team Analysis','Batsman Analysis','Bowler Analysis','Fielder Analysis')
)

team,player = helper.team_batsman_list(df)
bowler=helper.get_bowler(df)
fielder=helper.get_fielder(df)

if user_choice=='Batsman Analysis':
    st.sidebar.header('Batsman Analysis')
    selected_team=st.sidebar.selectbox('Select Team',team)
    selected_player=st.selectbox('Select Player',player)


    batsman_score,no_of_matches=helper.fetch_team_player(df,selected_team,selected_player)
    batsman_score.index=np.arange(1,len(batsman_score)+1)
    no_of_matches.index=np.arange(1,len(no_of_matches)+1)
    batsman_score.rename_axis("Rank",inplace=True)
    if(selected_team=='All Teams'):
        st.header("Runs Scored by a Player till IPL 2020")
    else:
        st.header("Run Scored for " + selected_team)
    st.table(batsman_score)
    if(selected_team=='All Teams'):
        st.header("No of matches Player have batted till IPL 2020")
    else:
        st.header("No of matches Player have batted for " + selected_team)
    st.table(no_of_matches)


if user_choice=='Bowler Analysis':
    st.sidebar.header('Bowler Analysis')
    selected_team=st.sidebar.selectbox('Select Team',team)
    selected_bowler=st.selectbox('Select Bowler',bowler)


    bowler_wicket,no_of_matches=helper.fetch_team_bowler(df,selected_team,selected_bowler)
    bowler_wicket.index=np.arange(1,len(bowler_wicket)+1)
    no_of_matches.index=np.arange(1,len(no_of_matches)+1)
    if(selected_team=='All Teams'):
        st.header("Wicket Taken by a Player till IPL 2020")
    else:
        st.header("Wicket Taken for " + selected_team)
    st.table(bowler_wicket)
    if(selected_team=='All Teams'):
        st.header("No of matches Player have bowled till IPL 2020")
    else:
        st.header("No of matches Player have bowled for " + selected_team)
    st.table(no_of_matches)

if(user_choice=='Fielder Analysis'):
    st.header('Fielder Analysis')
    st.markdown("""---""")
    selected_fielder=st.selectbox('Select Fielder',fielder)
    catches=helper.fetch_catches(df,selected_fielder)
    runouts=helper.fetch_runout(df,selected_fielder)
    stumping=helper.fetch_stumping(df,selected_fielder)
    catches.index=np.arange(1,len(catches)+1)
    runouts.index=np.arange(1,len(runouts)+1)
    stumping.index=np.arange(1,len(stumping)+1)
    if(selected_fielder=='All Fielder'):
        st.header("No of catches taken by all Fielders")
    else:
        st.header("No of catches taken")
    st.table(catches)
    if(selected_fielder=='All Fielder'):
        st.header("No of Runouts done by all Fielders ")
    else:
        st.header("No of Runouts done")
    st.table(runouts)
    if(selected_fielder=='All Fielder'):
        st.header("No of Stumping done by all Wicket Keepers ")
    else:
        st.header("No of Stumping done")
    st.table(stumping)

if(user_choice=='Team Analysis'):
    st.title("Team Analysis on Runs")
    team_table=helper.team_table(df)
    team_table.index=np.arange(1,len(team_table)+1)
    st.table(team_table)
    st.title("Team Analysis on Wicket")
    team_table_wicket=helper.team_table_wicket(df)

    st.table(team_table_wicket) 
    st.markdown("""---""")
    sixes_hit=helper.sixes_hit(df)
    sixes_conced=helper.sixes_conced(df)
    col1, col2 = st.columns(2)
    with col1:
        st.header("Sixes hitted")
        st.bar_chart(sixes_hit.set_index('Teams')['No of Sixes Hitted'])
    with col2:
        st.header("Sixes conceded")
        st.bar_chart(sixes_conced.set_index('Teams')['No of Sixes Conceded'])
    st.markdown("""---""")
    four_hit=helper.four_hit(df)
    four_conced=helper.four_conced(df)
    col1, col2 = st.columns(2)
    with col1:
        st.header("Fours hitted")
        st.bar_chart(four_hit.set_index('Teams')['No of Fours Hitted'], color="#FF5733")
    with col2:
        st.header("Fours conceded")
        st.bar_chart(four_conced.set_index('Teams')['No of Fours Conceded'], color="#FF5733")

if(user_choice=='Overall Analysis'):
    year=13
    no_of_matches=df['id'].unique().shape[0]
    no_of_batsman=df['batsman'].unique().shape[0]
    no_of_bowler=df['bowler'].unique().shape[0]
    temp=df['bowler'].unique().tolist()
    temp2=df['batsman'].unique().tolist()
    no_of_player=len(list(set(temp) | set(temp2)))
    no_of_sixes=df[(df['batsman_runs']==6) & (df['extra_runs']==0) & (df['non_boundary']==0)].shape[0]
    no_of_fours=df[(df['batsman_runs']==4) & (df['extra_runs']==0) & (df['non_boundary']==0)].shape[0]
    total_runs=df['total_runs'].sum()
    total_wickets=df[df['is_wicket']==1].shape[0]
    no_of_wides=df[df['extras_type']=='wides'].shape[0]
    no_of_noballs=df[df['extras_type']=='noballs'].shape[0]
    boundary_runs=no_of_fours*4+no_of_sixes*6
    extras=df['extra_runs'].sum()
    non_boundary_runs=total_runs-(boundary_runs+extras)
    st.title("Overall Analysis")
    st.markdown("""---""")

    col1,col2,col3=st.columns(3)
    with col1:
        st.header('Year Played')
        st.title('2008-20')
        
    with col2:
        st.header("Edition")
        st.title(year)     
    with col3:
        st.header('Matches ')
        st.title(no_of_matches)
    
    col1,col2,col3=st.columns(3)
    with col1:
        st.header("Player")
        st.title(no_of_player)
    with col2:
        st.header("Batsman")
        st.title(no_of_batsman)
    with col3:
        st.header('Bowler')
        st.title(no_of_bowler)

    col1,col2,col3=st.columns(3)
    with col1:
        st.header("Total Runs")
        st.title(total_runs)
    with col2:
        st.header("Sixes")
        st.title(no_of_sixes)
    with col3:
        st.header('Fours')
        st.title(no_of_fours)
    col1,col2,col3=st.columns(3)
    with col1:
        st.header("Total Wicket")
        st.title(total_wickets)
    with col2:
        st.header("No Balls")
        st.title(no_of_noballs)
    with col3:
        st.header('Wides')
        st.title(no_of_wides)

    batsman_career=df.groupby('batsman').sum()['batsman_runs'].sort_values(ascending=False).reset_index().head(3)
    batsman_career.columns=['Batsman Name','Total Runs Scored']
    batsman_career.index=np.arange(1,len(batsman_career)+1)

    excluded_dismissal=['run out','obstructing the field','retired hurt']
    bowler_career=df[~df['dismissal_kind'].isin(excluded_dismissal)].groupby('bowler').sum()['is_wicket'].sort_values(ascending=False).reset_index().head(3)
    bowler_career.columns=['Bowler Name','Total Wickets']
    bowler_career.index=np.arange(1,len(bowler_career)+1)

    st.markdown("""---""")
    st.title("Top 3 Scorer of All Time")
    st.table(batsman_career)
    st.title("Top 3 Wicket Taker of all Time")
    st.table(bowler_career)






    labels = ['Boundary Runs', 'extras','Non Boundary Runs']
    data=[boundary_runs,extras,non_boundary_runs]
    fig, ax = plt.subplots()
    ax.pie(data, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.markdown("""---""")
    st.title("Scoring details : ")
    st.pyplot(fig)

    wicket_type=df['dismissal_kind'].value_counts().tolist()
    labels=['caught', 'bowled', 'run out', 'lbw','stumped', 'caught and bowled', 'hit wicket', 'retired hurt','obstructing the field']
    fig, ax = plt.subplots() 
    wedges, texts, autotexts = ax.pie(wicket_type, autopct='%1.1f%%', startangle=90, pctdistance=0.85, labeldistance=1.1)
    flag=0
    for autotext in autotexts:
        flag=flag+1
        if(flag>=7):
            autotext.set_fontsize(0) 
         
    ax.legend(wedges, labels, loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    ax.axis('equal')
    st.markdown("""---""")
    st.title("Wicket details : ")
    st.pyplot(fig)









