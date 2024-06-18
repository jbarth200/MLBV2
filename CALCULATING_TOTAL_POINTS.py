import pandas as pd
from pandas import ExcelWriter
import time
import os
excel_data_df = pd.read_excel(r'C:\Users\joshb\PycharmProjects\MLB_V6\MLB_Schedule.xlsx', sheet_name='Sheet1', engine='openpyxl')
excel_data_df = excel_data_df.iloc[::-1]

print(excel_data_df)
print('Data Frame Above')
yahoot = len(excel_data_df)
print('Length Of Dataframe Below')
print(yahoot)
okay = 0
home_total_point_list = []



for games in excel_data_df.iterrows():
    yahoot -= 1
    print(yahoot)
    searching = excel_data_df.iloc[yahoot, 0]
    print(searching)
    searching_away = excel_data_df.iloc[yahoot, 1]
    print(searching_away)
    excel_data_df2 = pd.read_excel(r'C:\Users\joshb\PycharmProjects\MLB_V6\MLB_STATS_ALL.xlsx', sheet_name='Sheet1', engine='openpyxl')
    print(excel_data_df2)
    finding = excel_data_df2[excel_data_df2['TEAM:'] == searching].index
    finding_away = excel_data_df2[excel_data_df2['TEAM:'] == searching_away].index
    print(finding.values)
    home_team_games_played = (excel_data_df2.iloc[finding]["GAMES PLAYED:"])
    print(finding_away.values)
    print("WHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    away_team_games_played = (excel_data_df2.iloc[finding_away]["GAMES PLAYED:"])
    print(home_team_games_played.values)
    dddd = home_team_games_played
    print(away_team_games_played.values)
    home_team_total_points = (excel_data_df2.iloc[finding]["TOTAL RUNS BATTING:"])
    away_team_total_points = (excel_data_df2.iloc[finding_away]["TOTAL RUNS BATTING:"])
    print(home_team_total_points.values)
    print(away_team_total_points.values)

    hh = home_team_total_points.values / home_team_games_played.values
    aa = away_team_total_points.values / away_team_games_played.values
    print(hh)
    total_points_for_game = hh + aa
    home_total_point_list.append(total_points_for_game)


dataframe_schedule = pd.DataFrame({'PROJECTED POINTS:': home_total_point_list})
new_schedule_score = excel_data_df.merge(dataframe_schedule, left_index=True, right_index=True)
##new_schedule_score2 = excel_data_df.merge(dataframe_schedule2, left_index=True, right_index=True)
stats_doc = ExcelWriter(time.strftime('Total_Points_%Y_%m_%d.xlsx'), engine='openpyxl')
new_schedule_score.to_excel(stats_doc, sheet_name='Sheet1', index=False)
stats_doc.close()













