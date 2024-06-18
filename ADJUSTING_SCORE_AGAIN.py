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
test_home_team = []
test_away_team = []
home_total_pitches_pitching = []
away_total_pitches_pitching = []
away_pace_per_game_list = []
home_average_hits_batting = []
away_average_hits_batting = []
home_total_hits_batting = []
away_total_hits_batting = []
home_on_base_percent_batting = []
away_on_base_percent_batting = []
home_on_base_percent = []
away_on_base_percent = []
home_strikeout_batting = []
away_strikeout_batting = []
home_bases_batting = []
away_bases_batting = []







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
    print(finding)
    test_home_team.append(searching)
    test_away_team.append(searching_away)
    home_team_games_played = (excel_data_df2.iloc[finding]["GAMES PLAYED:"])
    home_team_total_points = (excel_data_df2.iloc[finding]["TOTAL RUNS BATTING:"])
    home_total_pitches_pitching = (excel_data_df2.iloc[finding]["TOTAL PITCHES PITCHING:"])
    home_total_rbi_batting = (excel_data_df2.iloc[finding]["TOTAL RBI BATTING:"])
    print(finding_away)
    away_team_total_points = (excel_data_df2.iloc[finding_away]["TOTAL RUNS BATTING:"])
    away_team_games_played = (excel_data_df2.iloc[finding_away]["GAMES PLAYED:"])
    away_total_pitches_pitching = (excel_data_df2.iloc[finding_away]["TOTAL PITCHES PITCHING:"])
    away_total_rbi_batting = (excel_data_df2.iloc[finding_away]["TOTAL RBI BATTING:"])
    home_slugging_on_base = (excel_data_df2.iloc[finding]["TOTAL BASE ON PLUS SLUGGING PERCENTAGE BATTING:"])
    away_slugging_on_base = (excel_data_df2.iloc[finding_away]["TOTAL BASE ON PLUS SLUGGING PERCENTAGE BATTING:"])
    home_average_hits_batting = (excel_data_df2.iloc[finding]["TOTAL AVERAGE HITS BATTING:"])
    away_average_hits_batting = (excel_data_df2.iloc[finding_away]["TOTAL AVERAGE HITS BATTING:"])
    home_total_hits_batting = (excel_data_df2.iloc[finding]["TOTAL HITS BATTING:"])
    away_total_hits_batting = (excel_data_df2.iloc[finding_away]["TOTAL HITS BATTING:"])
    home_on_base_percent_batting = (excel_data_df2.iloc[finding]["TOTAL ON BASE PERCENTAGE BATTING:"])
    away_on_base_percent_batting = (excel_data_df2.iloc[finding_away]["TOTAL ON BASE PERCENTAGE BATTING:"])
    home_on_base_percent = (excel_data_df2.iloc[finding]["ON BASE % PITCHING:"])
    away_on_base_percent = (excel_data_df2.iloc[finding_away]["ON BASE % PITCHING:"])
    home_strikeout_batting = (excel_data_df2.iloc[finding]["TOTAL STRIKE OUT BATTING:"])
    away_strikeout_batting = (excel_data_df2.iloc[finding_away]["TOTAL STRIKE OUT BATTING:"])
    home_bases_batting = (excel_data_df2.iloc[finding]["TOTAL BASES BATTING"])
    away_bases_batting = (excel_data_df2.iloc[finding_away]["TOTAL BASES BATTING"])


    home_triple_plate_batting = (excel_data_df2.iloc[finding]["TRIPLE PLATE APPEARANCES BATTING:"])
    away_triple_plate_batting = (excel_data_df2.iloc[finding_away]["TRIPLE PLATE APPEARANCES BATTING:"])


    home_team_ppg = home_team_total_points.values / home_team_games_played.values
    away_team_ppg = away_team_total_points.values / away_team_games_played.values

    ##THIS IS THE FORMULA FOR RETIREMENT!!!!

    print(home_team_ppg)
    print(away_team_ppg)

    totals = home_team_ppg + away_team_ppg
    print(totals)
    print("THEY ARE ABOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOVE")

    total_pitches_divided = home_total_pitches_pitching.values / away_total_pitches_pitching.values
    print(total_pitches_divided)

    if 0.97 <= total_pitches_divided <= 1.03:
        home_team_ppg = home_team_ppg + 0.25
        away_team_ppg = away_team_ppg + 0.25

    else:
        home_team_ppg = home_team_ppg - 0.25
        away_team_ppg = away_team_ppg - 0.25

    print(home_team_ppg)
    print(away_team_ppg)

    total_average_hits_divided = home_average_hits_batting.values / away_average_hits_batting.values

    if 0.96 <= total_average_hits_divided <= 1.04:
        home_team_ppg = home_team_ppg
        away_team_ppg = away_team_ppg

    else:
        home_team_ppg = home_team_ppg - 0.25
        away_team_ppg = away_team_ppg - 0.25

    if 0.95 <= total_average_hits_divided <= 1.05:
        home_team_ppg = home_team_ppg + 0.25
        away_team_ppg = away_team_ppg + 0.25

    else:
        home_team_ppg = home_team_ppg
        away_team_ppg = away_team_ppg

    print(home_team_ppg)
    print(away_team_ppg)

    total_hits_batting_divided = home_total_hits_batting.values / away_total_hits_batting.values

    if 0.94 <= total_hits_batting_divided <= 1.06:
        home_team_ppg = home_team_ppg + 0.25
        away_team_ppg = away_team_ppg + 0.25

    else:
        home_team_ppg = home_team_ppg
        away_team_ppg = away_team_ppg

    if 0.95 <= total_hits_batting_divided <= 1.05:
        home_team_ppg = home_team_ppg
        away_team_ppg = away_team_ppg

    else:
        home_team_ppg = home_team_ppg - 0.25
        away_team_ppg = away_team_ppg - 0.25

    total_on_base_precent_batting_divided = home_on_base_percent_batting.values / away_on_base_percent_batting.values


    if 0.96 <= total_on_base_precent_batting_divided <= 1.04:
        home_team_ppg = home_team_ppg
        away_team_ppg = away_team_ppg

    else:
        home_team_ppg = home_team_ppg - 0.25
        away_team_ppg = away_team_ppg - 0.25



    total_on_base_precent_divided = home_on_base_percent.values / away_on_base_percent.values


    if 0.94 <= total_on_base_precent_divided <= 1.06:
        home_team_ppg = home_team_ppg + 0.25
        away_team_ppg = away_team_ppg + 0.25

    else:
        home_team_ppg = home_team_ppg - 0.25
        away_team_ppg = away_team_ppg - 0.25



    total_strike_out_batting_divided = home_strikeout_batting.values / away_strikeout_batting.values


    if 0.93 <= total_strike_out_batting_divided <= 1.07:
        home_team_ppg = home_team_ppg + 0.25
        away_team_ppg = away_team_ppg + 0.25

    else:
        home_team_ppg = home_team_ppg - 0.25
        away_team_ppg = away_team_ppg - 0.25



    total_bases_batting_divided = home_bases_batting.values / away_bases_batting.values

    if 0.93 <= total_bases_batting_divided <= 1.07:
        home_team_ppg = home_team_ppg + 0.25
        away_team_ppg = away_team_ppg + 0.25

    else:
        home_team_ppg = home_team_ppg - 0.25
        away_team_ppg = away_team_ppg - 0.25

    print(home_team_ppg)
    print(away_team_ppg)



    game_total = home_team_ppg + away_team_ppg
    game_total2 = str(game_total)
    game_total2 = game_total2[1:]
    game_total2 = game_total2[:-1]
    try:
        game_total3 = float(game_total2)
    except ValueError:
        game_total3 = 0
    game_total4 = round(game_total3)
    total_point_list.append(game_total)

##total_point_list.reverse()

test_test = str(total_point_list)

test_points = total_point_list
test_home_team_over = test_home_team
test_away_team_over = test_away_team
print(test_points)
print("It's above before moving to Kivy File")
dataframe_schedule = pd.DataFrame({'GAME POINTS WITH FORMULA:': total_point_list})
##dataframe_schedule2 = pd.DataFrame({'PACE PER GAME:': pace_per_game_list})
##dataframe_schedule2 = dataframe_schedule2.sort_index(axis=1 ,ascending=False)
##dataframe_schedule2 = dataframe_schedule2.iloc[::-1]
dataframe_schedule = dataframe_schedule.sort_index(axis=1, ascending=False)
dataframe_schedule = dataframe_schedule.iloc[::-1]
new_schedule_score = excel_data_df.merge(dataframe_schedule, left_index=True, right_index=True)
##new_schedule_score2 = excel_data_df.merge(dataframe_schedule2, left_index=True, right_index=True)
stats_doc = ExcelWriter(time.strftime('Total_Points2_%Y_%m_%d.xlsx'), engine='openpyxl')
new_schedule_score.to_excel(stats_doc, sheet_name='Sheet1', index=False)
stats_doc.close()
##new_schedule_score2.to_excel(stats_doc, sheet_name='Sheet1', index=False)
##stats_doc.close()

excel_data_df2 = pd.read_excel(time.strftime('Total_Points2_%Y_%m_%d.xlsx'), sheet_name='Sheet1', engine='openpyxl')
excel_data_df2 = excel_data_df2.replace({'\\[':''}, regex=True)
excel_data_df2 = excel_data_df2.replace({'\\]':''}, regex=True)
excel_data_df2 = excel_data_df2.replace({"\\'":''}, regex=True)
excel_data_df2 = excel_data_df2.replace({'\\"':''}, regex=True)
stats_doc = ExcelWriter(time.strftime('Total_Points2_%Y_%m_%d.xlsx'), engine='openpyxl')
excel_data_df2.to_excel(stats_doc, sheet_name='Sheet1', index=False)
stats_doc.close()

