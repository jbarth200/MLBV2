import pandas as pd
from pandas import ExcelWriter
import numpy as np
import time
import os
excel_data_df = pd.read_excel(time.strftime('Total_Points2_%Y_%m_%d.xlsx'), sheet_name='Sheet1', engine='openpyxl')


print(excel_data_df)
print('Data Frame Above')
yahoot = len(excel_data_df)
print('Length Of Dataframe Below')
print(yahoot)
okay = 0

game_money_line_list = list()

for games in excel_data_df.iterrows():
    yahoot -= 1
    print(yahoot)
    searching = excel_data_df.iloc[yahoot, 1]
    print(searching)
    excel_data_df2 = pd.read_excel(r'C:\Users\joshb\PycharmProjects\MLB_V6\Money_Line_Draftkings.xlsx', sheet_name='Sheet1', engine='openpyxl')
    print(excel_data_df2)
    finding = excel_data_df2[excel_data_df2['AWAY TEAM:'] == searching].index
    print(finding)
    game_money_line = (excel_data_df2.iloc[finding]["MONEY LINE:"])
    game_money_line_list.append(game_money_line.values)




print(game_money_line_list)
game_money_line_list.reverse()

print("It's above before moving to Kivy File")
dataframe_schedule = pd.DataFrame({'MONEY LINE:': game_money_line_list})
##dataframe_schedule2 = pd.DataFrame({'PACE PER GAME:': pace_per_game_list})
##dataframe_schedule2 = dataframe_schedule2.sort_index(axis=1 ,ascending=False)
##dataframe_schedule2 = dataframe_schedule2.iloc[::-1]
dataframe_schedule = dataframe_schedule.sort_index(axis=1 ,ascending=False)
##dataframe_schedule = dataframe_schedule.iloc[::-1]
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





