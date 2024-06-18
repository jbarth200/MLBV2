import pandas as pd
from pandas import ExcelWriter
import numpy as np
import time
import os
excel_data_df = pd.read_excel(time.strftime('Total_Points_%Y_%m_%d.xlsx'), sheet_name='Sheet1', engine='openpyxl')
excel_data_df = excel_data_df.iloc[::-1]

print(excel_data_df)
print('Data Frame Above')
yahoot = len(excel_data_df)
print('Length Of Dataframe Below')
print(yahoot)
okay = 0
##global test
total_point_list = []
home_pace_per_game_list = []
home_team = []
away_team = []
home_team_shots_on_goal = []
away_team_oppg = []
away_pace_per_game_list = []

for games in excel_data_df.iterrows():
    yahoot -= 1
    print(yahoot)
    searching = excel_data_df.iloc[yahoot, 0]
    print(searching)
    searching_away = excel_data_df.iloc[yahoot, 1]
    print(searching_away)
    excel_data_df2 = pd.read_excel('NHL_STATS_ALL.xlsx', sheet_name='Sheet1', engine='openpyxl')
    print(excel_data_df2)
    finding = excel_data_df2[excel_data_df2['TEAM:'] == searching].index
    finding_away = excel_data_df2[excel_data_df2['TEAM:'] == searching_away].index
    print(finding)
    home_team.append(searching)
    away_team.append(searching_away)
    home_team_shots_on_goal = (excel_data_df2.iloc[finding]["TOTAL SHOTS ON GOAL:"])

    away_team_shots_on_goal = (excel_data_df2.iloc[finding_away]["TOTAL SHOTS ON GOAL:"])

    home_team_games_played = (excel_data_df2.iloc[finding]["GAMES PLAYED:"])
    print(finding_away.values)
    away_team_games_played = (excel_data_df2.iloc[finding_away]["GAMES PLAYED:"])
    print(home_team_games_played.values)
    dddd = home_team_games_played
    print(away_team_games_played.values)
    home_team_total_points = (excel_data_df2.iloc[finding]["TOTAL GOALS:"])
    away_team_total_points = (excel_data_df2.iloc[finding_away]["TOTAL GOALS:"])
    print(home_team_total_points.values)
    print(away_team_total_points.values)

    home_team_ppg = home_team_total_points.values / home_team_games_played.values
    away_team_ppg = away_team_total_points.values / away_team_games_played.values


    ##THIS IS THE FORMULA FOR RETIREMENT!!!!





    if home_team_shots_on_goal.values / away_team_shots_on_goal.values <= 0.95 or home_team_shots_on_goal.values / away_team_shots_on_goal.values >= 1.05:
        home_team_ppg = home_team_ppg - 0.5

    elif home_team_shots_on_goal.values / away_team_shots_on_goal.values <= 1.05 or home_team_shots_on_goal.values / away_team_shots_on_goal.values >= 0.95:
        home_team_ppg = home_team_ppg + 0.5

    if away_team_shots_on_goal.values / home_team_shots_on_goal.values <= 0.95 or away_team_shots_on_goal.values / home_team_shots_on_goal.values >= 1.05:
        away_team_ppg = away_team_ppg - 0.5
    elif away_team_shots_on_goal.values / home_team_shots_on_goal.values <= 1.05 or away_team_shots_on_goal.values / home_team_shots_on_goal.values >= 0.95:
        away_team_ppg = away_team_ppg + 0.5








    game_total = home_team_ppg + away_team_ppg

    total_point_list.append(game_total)

##total_point_list.reverse()

test = str(total_point_list)




points = total_point_list
home_team_over = home_team
away_team_over = away_team
print(points)
print("It's above before moving to Kivy File")
dataframe_schedule = pd.DataFrame({'GAME POINTS WITH FORMULA:': total_point_list})
##dataframe_schedule2 = pd.DataFrame({'PACE PER GAME:': pace_per_game_list})
##dataframe_schedule2 = dataframe_schedule2.sort_index(axis=1 ,ascending=False)
##dataframe_schedule2 = dataframe_schedule2.iloc[::-1]
dataframe_schedule = dataframe_schedule.sort_index(axis=1 ,ascending=False)
dataframe_schedule = dataframe_schedule.iloc[::-1]
new_schedule_score = excel_data_df.merge(dataframe_schedule, left_index=True, right_index=True)
##new_schedule_score2 = excel_data_df.merge(dataframe_schedule2, left_index=True, right_index=True)
stats_doc = ExcelWriter('New_Schedule22.xlsx', engine='openpyxl')
new_schedule_score.to_excel(stats_doc, sheet_name='Sheet1', index=False)
stats_doc.close()
##new_schedule_score2.to_excel(stats_doc, sheet_name='Sheet1', index=False)
##stats_doc.close()

os.rename('New_Schedule22.xlsx', time.strftime('Total_Points2_%Y_%m_%d.xlsx'))


