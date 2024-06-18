import time


import pandas as pd
from datetime import date, timedelta
from pandas import ExcelWriter
yesterday = date.today() - timedelta(+1)

import mysql


##Calculating ACTUAL OVER_Under
excel_data_df2 = pd.read_excel(yesterday.strftime('Total_Points_PREV_DAY_%Y_%m_%d.xlsx'), sheet_name='Sheet1', engine='openpyxl')
excel_data_df2 = excel_data_df2.iloc[::-1]

print(excel_data_df2)
print('Data Frame Above')
yahoot = len(excel_data_df2)
print('Length Of Dataframe Below')
print(yahoot)
okay = 0
win_or_lose_list = []

for games in excel_data_df2.iterrows():
    overr_or_under = ''
    yahoot -= 1
    print(yahoot)
    searching = excel_data_df2.iloc[yahoot, 0]
    print(searching)
    print(excel_data_df2)
    finding = excel_data_df2[excel_data_df2['HOME TEAM:'] == searching].index
    print(finding)
    guessed_over_under = (excel_data_df2.iloc[finding]["MONEY LINE:"])
    print(guessed_over_under.values)
    actual_over_under = (excel_data_df2.iloc[finding]["ACTUAL GAME POINTS:"])
    if guessed_over_under.size > 0 and guessed_over_under.values < actual_over_under.values:
        overr_or_under = "OVER"
    else:
        None

    if guessed_over_under.size > 0 and guessed_over_under.values > actual_over_under.values:
        overr_or_under = "UNDER"
    else:
        None

    win_or_lose_list.append(overr_or_under)


win_or_lose_list.reverse()


dataframe_schedule2 = pd.DataFrame({'ACTUAL OVER UNDER RESULT:': win_or_lose_list})
dataframe_schedule2 = dataframe_schedule2.sort_index(axis=1 ,ascending=True)
new_schedule_score2 = excel_data_df2.merge(dataframe_schedule2, left_index=True, right_index=True)
stats_doc = ExcelWriter(yesterday.strftime('Total_Points_PREV_DAY_%Y_%m_%d.xlsx'), engine='openpyxl')
new_schedule_score2.to_excel(stats_doc, sheet_name='Sheet1', index=False)
stats_doc.close()

##Now SAYING WIN OR LOSE

excel_data_df2 = pd.read_excel(yesterday.strftime('Total_Points_PREV_DAY_%Y_%m_%d.xlsx'), sheet_name='Sheet1', engine='openpyxl')
excel_data_df2 = excel_data_df2.iloc[::-1]

print(excel_data_df2)
print('Data Frame Above')
yahoot = len(excel_data_df2)
print('Length Of Dataframe Below')
print(yahoot)
okay = 0
win_or_lose_list = []

win_list = []

for games in excel_data_df2.iterrows():
    yahoot -= 1
    print(yahoot)
    searching = excel_data_df2.iloc[yahoot, 0]
    print(searching)
    print(excel_data_df2)
    finding = excel_data_df2[excel_data_df2['HOME TEAM:'] == searching].index
    print(finding)
    guessed_over_under = (excel_data_df2.iloc[finding]["OVER OR UNDER"])
    print(guessed_over_under.values)
    actual_over_under = (excel_data_df2.iloc[finding]["ACTUAL OVER UNDER RESULT:"])
    print(actual_over_under.values)

    if guessed_over_under.values == actual_over_under.values or guessed_over_under.values == actual_over_under.values:
        overr_or_under = "Win"
    else:
        overr_or_under = "Lose"

    print("HERE ARE THE REULTS" + overr_or_under)

    win_or_lose_list.append(overr_or_under)

    if overr_or_under == "Win":
        win_list.append('1')
print(" WIN LIST HEREERERERERERER")
print(win_list)
wins = len(win_list)
print(wins)
howmany = len(excel_data_df2)
print(yahoot)

percentage_won = wins / howmany

print(percentage_won)

win_or_lose_list.reverse()
dataframe_schedule2 = pd.DataFrame({'Win Or Lose:': win_or_lose_list, "Percentage Won:": percentage_won})
dataframe_schedule2 = dataframe_schedule2.sort_index(axis=1, ascending=True)
new_schedule_score2 = excel_data_df2.merge(dataframe_schedule2, left_index=True, right_index=True)
stats_doc = ExcelWriter(yesterday.strftime('Total_Points_PREV_DAY_%Y_%m_%d.xlsx'), engine='openpyxl')
new_schedule_score2.to_excel(stats_doc, sheet_name='Sheet1', index=False)
stats_doc.close()






import pandas as pd
from pandas import ExcelWriter


import time

from datetime import date, timedelta
import os
yesterday = date.today() - timedelta(1)
##os.rename('New_Schedule2_Previous_Day.xlsx', yesterday.strftime('Previous_Day_Totals_%Y_%m_%d.xlsx'))
##os.rename('New_Schedule2.xlsx', 'Previous_Day_Totals.xlsx')


excel_data_df = pd.read_excel(yesterday.strftime('Total_Points_PREV_DAY_%Y_%m_%d.xlsx'), sheet_name='Sheet1', engine='openpyxl')


print(excel_data_df)
print('Data Frame Above')
yahoot = len(excel_data_df)
print('Length Of Dataframe Below')
print(yahoot)
previous_day_point_total = []
previous_day_point_total_correct = []
previous_day_home_total = []
previous_day_away_total = []


home_total_average_hits_batting = []
away_total_average_hits_batting = []
home_total_at_bats = []
away_total_at_bats = []
home_total_runs_batting = []
away_total_runs_batting = []
home_total_hits_batting = []
away_total_hits_batting = []
home_doubles_batting = []
away_doubles_batting = []
home_triples_batting = []
away_triples_batting = []
home_rbi_batting = []
away_rbi_batting = []
home_hr_batting = []
away_hr_batting = []
home_strikeout_batting = []
away_strikeout_batting = []
home_on_base_percent_batting = []
away_on_base_percent_batting = []
home_base_on_slugging_batting = []
away_base_on_slugging_batting = []
home_bases_batting = []
away_bases_batting = []

home_triple_plate_appearances_batting = []
away_triple_plate_appearances_batting = []
home_innings_pitching = []
away_innings_pitching = []
home_runs_pitching = []
away_runs_pitching = []

home_on_base_pitching = []
away_on_base_pitching = []
home_doubles_pitching = []
away_doubles_pitching = []
home_triples_pitching = []
away_triples_pitching = []

home_pitches_pitching = []
away_pitches_pitching = []
home_catches_fielding = []
away_catches_fielding = []
home_errors_fielding = []
away_errors_fielding = []

home_on_base_percent_pitching = []
away_on_base_percent_pitching = []
home_assists_fielding = []
away_assists_fielding = []
home_fielding_percent = []
away_fielding_percent = []


for games in excel_data_df.iterrows():
    yahoot -= 1
    print(yahoot)
    searching_home_points_previous_day = excel_data_df.iloc[yahoot, 0]
    print(searching_home_points_previous_day)
    searching_away_points_previous_day = excel_data_df.iloc[yahoot, 1]
    print(searching_away_points_previous_day)
    excel_data_df3 = pd.read_excel(r'C:\Users\joshb\PycharmProjects\MLB_V6\MLB_STATS.xlsx', sheet_name='Sheet1', engine='openpyxl')
    finding_home_pace_ppp = excel_data_df3[excel_data_df3['TEAM:'] == searching_home_points_previous_day].index
    finding_away_pace_ppp = excel_data_df3[excel_data_df3['TEAM:'] == searching_away_points_previous_day].index











    home_total_average_hits_batting_to_list = (excel_data_df3.iloc[finding_home_pace_ppp]["TOTAL AVERAGE HITS BATTING:"])
    ##home_team_ppp_to_list = (excel_data_df3.iloc[finding_home_pace_ppp]["POINTS PER POSSESSION:"])
    away_total_average_hits_batting_to_list = (excel_data_df3.iloc[finding_away_pace_ppp]["TOTAL AVERAGE HITS BATTING:"])
    ##away_team_ppp_to_list = (excel_data_df3.iloc[finding_away_pace_ppp]["POINTS PER POSSESSION:"])
    ##previous_day_away_total.append(home_team_ppg.values)
    ##previous_day_home_total.append(away_team_ppg.values)
    home_total_average_hits_batting.append(home_total_average_hits_batting_to_list.values)
    ##home_team_ppp_list.append(home_team_ppp_to_list.values)
    away_total_average_hits_batting.append(away_total_average_hits_batting_to_list.values)
    ##away_team_ppp_list.append(away_team_ppp_to_list.values)
    home_total_at_bats_to_list = (excel_data_df3.iloc[finding_home_pace_ppp]["TOTAL AT BATS:"])
    home_total_at_bats.append(home_total_at_bats_to_list.values)
    away_total_at_bats_to_list = (excel_data_df3.iloc[finding_away_pace_ppp]["TOTAL AT BATS:"])
    away_total_at_bats.append(away_total_at_bats_to_list.values)
    home_total_runs_batting_to_list = (excel_data_df3.iloc[finding_home_pace_ppp]["TOTAL RUNS BATTING:"])
    home_total_runs_batting.append(home_total_runs_batting_to_list.values)
    away_total_runs_batting_to_list = (excel_data_df3.iloc[finding_away_pace_ppp]["TOTAL RUNS BATTING:"])
    away_total_runs_batting.append(away_total_runs_batting_to_list.values)
    home_total_hits_batting_to_list = (excel_data_df3.iloc[finding_home_pace_ppp]["TOTAL HITS BATTING:"])
    home_total_hits_batting.append(home_total_hits_batting_to_list.values)
    away_total_hits_batting_to_list = (excel_data_df3.iloc[finding_away_pace_ppp]["TOTAL HITS BATTING:"])
    away_total_hits_batting.append(away_total_hits_batting_to_list.values)
    home_doubles_batting_to_list = (excel_data_df3.iloc[finding_home_pace_ppp]["TOTAL DOUBLES BATTING:"])
    home_doubles_batting.append(home_doubles_batting_to_list.values)
    away_doubles_batting_to_list = (excel_data_df3.iloc[finding_away_pace_ppp]["TOTAL DOUBLES BATTING:"])
    away_doubles_batting.append(away_doubles_batting_to_list.values)
    home_triples_batting_to_list = (excel_data_df3.iloc[finding_home_pace_ppp]["TOTAL TRIPLES BATTING:"])
    home_triples_batting.append(home_triples_batting_to_list.values)
    away_triples_batting_to_list = (excel_data_df3.iloc[finding_away_pace_ppp]["TOTAL TRIPLES BATTING:"])
    away_triples_batting.append(away_triples_batting_to_list.values)
    home_rbi_batting_to_list = (excel_data_df3.iloc[finding_home_pace_ppp]["TOTAL RBI BATTING:"])
    home_rbi_batting.append(home_rbi_batting_to_list.values)
    away_rbi_batting_to_list = (excel_data_df3.iloc[finding_away_pace_ppp]["TOTAL RBI BATTING:"])
    away_rbi_batting.append(away_rbi_batting_to_list.values)


    home_hr_batting_to_list = (excel_data_df3.iloc[finding_home_pace_ppp]["TOTAL HOME RUN BATTING:"])
    home_hr_batting.append(home_hr_batting_to_list.values)
    away_hr_batting_to_list = (excel_data_df3.iloc[finding_away_pace_ppp]["TOTAL HOME RUN BATTING:"])
    away_hr_batting.append(away_hr_batting_to_list.values)
    home_strikeout_batting_to_list = (excel_data_df3.iloc[finding_home_pace_ppp]["TOTAL STRIKE OUT BATTING:"])
    home_strikeout_batting.append(home_strikeout_batting_to_list.values)
    away_strikeout_batting_to_list = (excel_data_df3.iloc[finding_away_pace_ppp]["TOTAL STRIKE OUT BATTING:"])
    away_strikeout_batting.append(away_strikeout_batting_to_list.values)
    home_on_base_percent_batting_to_list = (excel_data_df3.iloc[finding_home_pace_ppp]["TOTAL ON BASE PERCENTAGE BATTING:"])
    home_on_base_percent_batting.append(home_on_base_percent_batting_to_list.values)
    away_on_base_percent_batting_to_list = (excel_data_df3.iloc[finding_away_pace_ppp]["TOTAL ON BASE PERCENTAGE BATTING:"])
    away_on_base_percent_batting.append(away_on_base_percent_batting_to_list.values)
    home_base_on_slugging_batting_to_list2 = (excel_data_df3.iloc[finding_home_pace_ppp]["TOTAL BASE ON PLUS SLUGGING PERCENTAGE BATTING:"])
    home_base_on_slugging_batting.append(home_base_on_slugging_batting_to_list2.values)
    away_base_on_slugging_batting_to_list2 = (excel_data_df3.iloc[finding_away_pace_ppp]["TOTAL BASE ON PLUS SLUGGING PERCENTAGE BATTING:"])
    away_base_on_slugging_batting.append(away_base_on_slugging_batting_to_list2.values)
    home_bases_batting_to_list = (excel_data_df3.iloc[finding_home_pace_ppp]["TOTAL BASES BATTING"])
    home_bases_batting.append(home_bases_batting_to_list.values)
    away_bases_batting_to_list = (excel_data_df3.iloc[finding_away_pace_ppp]["TOTAL BASES BATTING"])
    away_bases_batting.append(away_bases_batting_to_list.values)


    home_triple_plate_appearances_batting_to_list = (excel_data_df3.iloc[finding_home_pace_ppp]["TRIPLE PLATE APPEARANCES BATTING:"])
    home_triple_plate_appearances_batting.append(home_triple_plate_appearances_batting_to_list.values)
    away_triple_plate_appearances_batting_to_list = (excel_data_df3.iloc[finding_away_pace_ppp]["TRIPLE PLATE APPEARANCES BATTING:"])
    away_triple_plate_appearances_batting.append(away_triple_plate_appearances_batting_to_list.values)
    home_innings_pitching_to_list = (excel_data_df3.iloc[finding_home_pace_ppp]["INNINGS PITCHED:"])
    home_innings_pitching.append(home_innings_pitching_to_list.values)
    away_innings_pitching_to_list = (excel_data_df3.iloc[finding_away_pace_ppp]["INNINGS PITCHED:"])
    away_innings_pitching.append(away_innings_pitching_to_list.values)
    home_runs_pitching_to_list = (excel_data_df3.iloc[finding_home_pace_ppp]["TOTAL RUNS PITCHING:"])
    home_runs_pitching.append(home_runs_pitching_to_list.values)
    away_runs_pitching_to_list = (excel_data_df3.iloc[finding_away_pace_ppp]["TOTAL RUNS PITCHING:"])
    away_runs_pitching.append(away_runs_pitching_to_list.values)
    home_on_base_pitching_to_list = (excel_data_df3.iloc[finding_home_pace_ppp]["ON BASE % PITCHING:"])
    home_on_base_pitching.append(home_on_base_pitching_to_list.values)
    away_on_base_pitching_to_list = (excel_data_df3.iloc[finding_away_pace_ppp]["ON BASE % PITCHING:"])
    away_on_base_pitching.append(away_on_base_pitching_to_list.values)
    home_doubles_pitching_to_list = (excel_data_df3.iloc[finding_home_pace_ppp]["DOUBLES PITCHING:"])
    home_doubles_pitching.append(home_doubles_pitching_to_list.values)
    away_doubles_pitching_to_list = (excel_data_df3.iloc[finding_away_pace_ppp]["DOUBLES PITCHING:"])
    away_doubles_pitching.append(away_doubles_pitching_to_list.values)
    home_triples_pitching_to_list = (excel_data_df3.iloc[finding_home_pace_ppp]["TRIPLES PITCHING:"])
    home_triples_pitching.append(home_triples_pitching_to_list.values)
    away_triples_pitching_to_list = (excel_data_df3.iloc[finding_away_pace_ppp]["TRIPLES PITCHING:"])
    away_triples_pitching.append(away_triples_pitching_to_list.values)
    home_pitches_pitching_to_list = (excel_data_df3.iloc[finding_home_pace_ppp]["TOTAL PITCHES PITCHING:"])
    home_pitches_pitching.append(home_pitches_pitching_to_list.values)
    away_pitches_pitching_to_list = (excel_data_df3.iloc[finding_away_pace_ppp]["TOTAL PITCHES PITCHING:"])
    away_pitches_pitching.append(away_pitches_pitching_to_list.values)
    home_catches_fielding_to_list = (excel_data_df3.iloc[finding_home_pace_ppp]["TOTAL CATCHES:"])
    home_catches_fielding.append(home_catches_fielding_to_list.values)
    away_catches_fielding_to_list = (excel_data_df3.iloc[finding_away_pace_ppp]["TOTAL CATCHES:"])
    away_catches_fielding.append(away_catches_fielding_to_list.values)
    home_on_base_percent_pitching_to_list = (excel_data_df3.iloc[finding_home_pace_ppp]["ON BASE % PITCHING:"])
    home_on_base_percent_pitching.append(home_on_base_percent_pitching_to_list.values)
    away_on_base_percent_pitching_to_list = (excel_data_df3.iloc[finding_away_pace_ppp]["ON BASE % PITCHING:"])
    away_on_base_percent_pitching.append(away_on_base_percent_pitching_to_list.values)
    home_assists_fielding_to_list = (excel_data_df3.iloc[finding_home_pace_ppp]["TOTAL ASSISTS FIELDING:"])
    home_assists_fielding.append(home_assists_fielding_to_list.values)
    away_assists_fielding_to_list = (excel_data_df3.iloc[finding_away_pace_ppp]["TOTAL ASSISTS FIELDING:"])
    away_assists_fielding.append(away_assists_fielding_to_list.values)
    home_fielding_percent_to_list = (excel_data_df3.iloc[finding_home_pace_ppp]["FIELDING PERCENT:"])
    home_fielding_percent.append(home_fielding_percent_to_list.values)
    away_fielding_percent_to_list = (excel_data_df3.iloc[finding_away_pace_ppp]["FIELDING PERCENT:"])
    away_fielding_percent.append(away_fielding_percent_to_list.values)
    home_errors_fielding_to_list = (excel_data_df3.iloc[finding_home_pace_ppp]["TOTAL ERRORS FIELDING:"])
    home_errors_fielding.append(home_errors_fielding_to_list.values)
    away_errors_fielding_to_list = (excel_data_df3.iloc[finding_away_pace_ppp]["TOTAL ERRORS FIELDING:"])
    away_errors_fielding.append(away_errors_fielding_to_list.values)







##previous_day_point_total_correct = previous_day_point_total.reverse()

import sqlalchemy

database_username = 'root'
database_password = ''
database_ip = 'localhost'
database_name = 'mlb_24'
database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                               format(database_username, database_password,
                                                    database_ip, database_name))


dataframe_schedule = pd.DataFrame({'HOME AVERAGE HITS BATTING:': home_total_average_hits_batting,
                                   'HOME TOTAL RUNS BATTING:': home_total_runs_batting, 'HOME HITS BATTING:': home_total_hits_batting,
                                   'HOME TRIPLES BATTING:': home_triples_batting, 'HOME RBI BATTING:': home_rbi_batting,
                                   'AWAY AVERAGE HITS BATTING:': away_total_average_hits_batting, 'AWAY TOTAL RUNS BATTING:': away_total_runs_batting,
                                   'AWAY HITS BATTING:': away_total_hits_batting, 'AWAY TRIPLES BATTING:': away_triples_batting,
                                   'AWAY RBI BATTING:': away_rbi_batting, "HOME TRIPLE PLATE APPERANACES BATTING:": home_triple_plate_appearances_batting,
                                   "AWAY TRIPLE PLATE APPERANACES BATTING:": away_triple_plate_appearances_batting, "HOME INNINGS PITCHED:": home_innings_pitching,
                                   "AWAY INNINGS PITCHED:": away_innings_pitching, "HOME RUNS PITCHING:": home_runs_pitching,
                                   "AWAY RUNS PITCHING:": away_runs_pitching, "HOME ON BASE PERCENT:": home_on_base_pitching,
                                   "AWAY ON BASE PERCENT:": away_on_base_pitching, "HOME DOUBLES PITCHING:": home_doubles_pitching,
                                   "AWAY DOUBLES PITCHING:": away_doubles_pitching, "HOME TRIPLE PITCHES:": home_triples_pitching,
                                   "AWAY TRIPLE PITCHES:": away_triples_pitching, "HOME PITCHES PITCHING": home_pitches_pitching,
                                   "AWAY PITCHES PITCHING:": away_pitches_pitching, "HOME TOTAL CATCHES": home_catches_fielding,
                                   "AWAY TOTAL CATCHES:": away_catches_fielding, "HOME TOTAL ERRORS:": home_errors_fielding,
                                   "AWAY TOTAL ERRORS:": away_errors_fielding, "HOME ASSISTS FIELDING:": home_assists_fielding,
                                   "AWAY ASSISTS FIELDING:": away_assists_fielding, "HOME FIELDING PERCENT:": home_fielding_percent,
                                   "AWAY FIELDING PERCENT:": away_fielding_percent, "HOME TOTAL AT BAT:": home_total_at_bats,
                                   "AWAY TOTAL AT BAT:": away_total_at_bats, "HOME DOUBLES BATTING:": home_doubles_batting,
                                   "AWAY DOUBLES BATTING:": away_doubles_batting, "HOME STRIKEOUT BATTING:":home_strikeout_batting,
                                   "AWAY STRIKEOUT BATTING:": away_strikeout_batting, "HOME ON BASE PERCENT BATTING:": home_on_base_percent_batting,
                                   "AWAY ON BASE PERCENT BATTING:": away_on_base_percent_batting, "HOME ON BASE PLUS SLUGGING:": home_base_on_slugging_batting,
                                   "AWAY ON BASE PLUS SLUGGING:": away_base_on_slugging_batting, "HOME TOTAL BASES BATTING:": home_bases_batting,
                                   "AWAY TOTAL BASES BATTING:": away_bases_batting, })
dataframe_schedule = dataframe_schedule.sort_index(axis=1 ,ascending=True)
dataframe_schedule = dataframe_schedule.iloc[::-1].reset_index(drop=True)
new_schedule_score = excel_data_df.merge(dataframe_schedule, left_index=True, right_index=True)
stats_doc = ExcelWriter(yesterday.strftime('Total_Points_PREV_DAY_%Y_%m_%d.xlsx'), engine='openpyxl')
new_schedule_score.to_excel(stats_doc, sheet_name='Sheet1', index=False)
stats_doc.close()


excel_data_df2 = pd.read_excel(yesterday.strftime('Total_Points_PREV_DAY_%Y_%m_%d.xlsx'), sheet_name='Sheet1', engine='openpyxl')
excel_data_df2 = excel_data_df2.replace({'\\[':''}, regex=True)
excel_data_df2 = excel_data_df2.replace({'\\]':''}, regex=True)
excel_data_df2 = excel_data_df2.replace({"\\'":''}, regex=True)
stats_doc = ExcelWriter(yesterday.strftime('Total_Points_PREV_DAY_%Y_%m_%d.xlsx'), engine='openpyxl')
excel_data_df2.to_excel(stats_doc, sheet_name='Sheet1', index=False)
stats_doc.close()
excel_data_df4 = pd.read_excel(yesterday.strftime('Total_Points_PREV_DAY_%Y_%m_%d.xlsx'), sheet_name='Sheet1', engine='openpyxl')







excel_data_df5 = pd.read_excel(yesterday.strftime('Total_Points_PREV_DAY_%Y_%m_%d.xlsx'), sheet_name='Sheet1', engine='openpyxl')


import datetime


today = datetime.date.today()

yesterday = today - datetime.timedelta(days=1)
dates = []
for teams in excel_data_df5.iterrows():
    dates.append(yesterday)



dataframe_date = pd.DataFrame({'DATE:': dates})
new_schedule_score = pd.concat([excel_data_df5, dataframe_date], axis=1)
stats_doc = ExcelWriter(yesterday.strftime('Total_Points_PREV_DAY_%Y_%m_%d_With_Date.xlsx'), engine='openpyxl')
new_schedule_score.to_excel(stats_doc, sheet_name='Sheet1', index=False)
stats_doc.close()



excel_data_df2 = pd.read_excel(yesterday.strftime('Total_Points_PREV_DAY_%Y_%m_%d_With_Date.xlsx'), sheet_name='Sheet1', engine='openpyxl')
excel_data_df2 = excel_data_df2.replace({'\\[':''}, regex=True)
excel_data_df2 = excel_data_df2.replace({'\\]':''}, regex=True)
excel_data_df2 = excel_data_df2.replace({"\\'":''}, regex=True)
stats_doc = ExcelWriter(yesterday.strftime('Total_Points_PREV_DAY_%Y_%m_%d_With_Date.xlsx'), engine='openpyxl')
excel_data_df2.to_excel(stats_doc, sheet_name='Sheet1', index=False)
stats_doc.close()
excel_data_df4 = pd.read_excel(yesterday.strftime('Total_Points_PREV_DAY_%Y_%m_%d_With_Date.xlsx'), sheet_name='Sheet1', engine='openpyxl')
excel_data_df4.to_sql(con=database_connection, name='previous_losses_mlb_v5_with_date', if_exists='replace', index=False)
excel_data_df4.to_sql(con=database_connection, name='previous_losses_mlb_v5_with_date_agg', if_exists='replace', index=False)



away_team_pitcher = []
home_team_pitcher = []
yeet = 0


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mlb_24"
)


mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM previous_losses_mlb_v5_with_date")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

val = myresult

mycursor.execute("INSERT INTO previous_losses_mlb_v5_with_date_agg SELECT * FROM previous_losses_mlb_v5_with_date")

mydb.commit()






excel_data_df = pd.read_excel(yesterday.strftime('Total_Points_PREV_DAY_%Y_%m_%d_With_Date.xlsx'), sheet_name='Sheet1', engine='openpyxl')

away_team = []
home_team = []
for games in excel_data_df.iterrows():
    yahoot -= 1
    print(yahoot)
    searching_home_points_previous_day = excel_data_df.iloc[yahoot, 0]
    print(searching_home_points_previous_day)
    searching_away_points_previous_day = excel_data_df.iloc[yahoot, 1]
    print(searching_away_points_previous_day)

    print('WELL HERE It IS JEFFREY')
    data1 = str(searching_away_points_previous_day)
    data2 = str(searching_away_points_previous_day)
    values = (data1, data2)
    mycursor = mydb.cursor()

    sql = "SELECT `AWAY PITCHER:` FROM `mlb_starting_pitchers` WHERE `AWAY TEAM:` = %s OR `HOME TEAM:` = %s"

    mycursor.execute(sql, values)
    myresult = mycursor.fetchall()
    away_team_pitcher.append(myresult)

    data3 = str(searching_home_points_previous_day)
    data4 = str(searching_home_points_previous_day)
    values2 = (data3, data4)
    mycursor = mydb.cursor()

    sql2 = "SELECT `HOME PITCHER:` FROM `mlb_starting_pitchers` WHERE `HOME TEAM:` = %s OR `AWAY TEAM:` = %s"

    mycursor.execute(sql2, values2)
    myresult2 = mycursor.fetchall()
    home_team_pitcher.append(myresult2)

    sql = "SELECT `AWAY TEAM:` FROM `mlb_starting_pitchers` WHERE `AWAY TEAM:` = %s OR `HOME TEAM:` = %s"

    mycursor.execute(sql, values)
    myresult = mycursor.fetchall()
    away_team.append(myresult)

    data1 = searching_home_points_previous_day[yeet]
    data2 = searching_home_points_previous_day[yeet]
    values = (data1, data2)
    mycursor = mydb.cursor()

    sql = "SELECT `HOME TEAM:` FROM `mlb_starting_pitchers` WHERE `AWAY TEAM:` = %s OR `HOME TEAM:` = %s"

    mycursor.execute(sql, values)
    myresult = mycursor.fetchall()
    home_team.append(myresult)



excel_data_df = pd.DataFrame({'HOME TEAM:': home_team, 'HOME TEAM PITCHER:': home_team_pitcher, 'AWAY TEAM:': away_team, 'AWAY TEAM PITCHER:': away_team_pitcher })
excel_data_df = excel_data_df.replace({'\\"':''}, regex=True)
excel_data_df = excel_data_df.replace({'\\]':''}, regex=True)
excel_data_df = excel_data_df.replace({'\\[':''}, regex=True)
excel_data_df = excel_data_df.replace({"\\'":''}, regex=True)
print(excel_data_df)
excel_data_df = excel_data_df.sort_values(by=['HOME TEAM:'], ascending=True)
del excel_data_df['HOME TEAM:']
del excel_data_df['AWAY TEAM:']
stats_doc = ExcelWriter(yesterday.strftime('Total_Points_PREV_DAY_%Y_%m_%d_With_Date_With_Pitcher.xlsx'), engine='openpyxl')
excel_data_df.to_excel(stats_doc, sheet_name='Sheet1', index=False)
stats_doc.close()


excel_data_df2 = pd.read_excel(yesterday.strftime('Total_Points_PREV_DAY_%Y_%m_%d_With_Date.xlsx'), sheet_name='Sheet1', engine='openpyxl')
print(excel_data_df2)
excel_data_df2 = excel_data_df2.sort_values(by=['HOME TEAM:'], ascending=True)
stats_doc = ExcelWriter(yesterday.strftime('Total_Points_PREV_DAY_%Y_%m_%d_With_Date.xlsx'), engine='openpyxl')
excel_data_df2.to_excel(stats_doc, sheet_name='Sheet1', index=False)
stats_doc.close()




new_schedule_score = pd.concat([excel_data_df.reset_index(drop=True), excel_data_df2.reset_index(drop=True)], axis=1)



#new_schedule_score = excel_data_df.merge(dataframe_schedule, left_index=True, right_index=True)
stats_doc = ExcelWriter(yesterday.strftime('Total_Points_PREV_DAY_%Y_%m_%d_With_Date_With_Pitcher.xlsx'), engine='openpyxl')
new_schedule_score.to_excel(stats_doc, sheet_name='Sheet1', index=False)
stats_doc.close()




excel_data_df4 = pd.read_excel(yesterday.strftime('Total_Points_PREV_DAY_%Y_%m_%d_With_Date_With_Pitcher.xlsx'), sheet_name='Sheet1', engine='openpyxl')
excel_data_df4.to_sql(con=database_connection, name='previous_losses_mlb_v5_with_date_with_pitcher', if_exists='replace', index=False)
excel_data_df4.to_sql(con=database_connection, name='previous_losses_mlb_v5_with_date_with_pitcher_agg', if_exists='replace', index=False)



mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mlb_24"
)


mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM previous_losses_mlb_v5_with_date_with_pitcher")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

val = myresult

mycursor.execute("INSERT INTO previous_losses_mlb_v5_with_date_with_pitcher_agg SELECT * FROM previous_losses_mlb_v5_with_date_with_pitcher")

mydb.commit()