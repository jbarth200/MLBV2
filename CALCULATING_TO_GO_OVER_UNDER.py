import pandas as pd
from pandas import ExcelWriter
import time
import numpy as np
import sqlalchemy

database_username = 'root'
database_password = ''
database_ip = 'localhost'
database_name = 'mlb_24'
database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                               format(database_username, database_password,
                                                    database_ip, database_name))
## CALCULATING IF I SHOULD GO OVER OR UNDER


excel_data_df2 = pd.read_excel(time.strftime('Total_Points2_%Y_%m_%d.xlsx'), sheet_name='Sheet1', engine='openpyxl')
df2 = excel_data_df2.apply(lambda x: pd.to_numeric(x.astype(str).str.replace(',',''), errors='coerce'))
df3 = df2.fillna(excel_data_df2)
stats_doc = ExcelWriter(time.strftime('Total_Points2_%Y_%m_%d.xlsx'), engine='openpyxl')
df3.to_excel(stats_doc, sheet_name='Sheet1', index=False)
stats_doc.close()



excel_data_df2 = pd.read_excel(time.strftime('Total_Points2_%Y_%m_%d.xlsx'), sheet_name='Sheet1', engine='openpyxl')


print(excel_data_df2)
print('Data Frame Above')
yahoot = len(excel_data_df2)
print('Length Of Dataframe Below')
print(yahoot)
okay = 0

over_or_under_list = []

total_point_list = []
money_line_list = []


for games in excel_data_df2.iterrows():
    yahoot -= 1
    print(yahoot)
    searching = excel_data_df2.iloc[yahoot, 0]
    print(searching)
    ##searching_away = excel_data_df.iloc[yahoot, 1]
    ##print(searching_away)
    print(excel_data_df2)
    finding = excel_data_df2[excel_data_df2['HOME TEAM:'] == searching].index
    ##finding_away = excel_data_df2[excel_data_df2['TEAM:'] == searching_away].index
    print(finding)
    total_points = (excel_data_df2.iloc[finding]["GAME POINTS WITH FORMULA:"])
    ##print(finding_away)
    ##away_team_ppg = (excel_data_df2.iloc[finding_away]["POINTS PER GAME:"])
    print(total_points.values)
    ##print(away_team_ppg.values)
    ##game_total = home_team_ppg.values + away_team_ppg.values
    ##total_point_list.append(game_total)
    money_line = (excel_data_df2.iloc[finding]["MONEY LINE:"])
    total_point_list.append(total_points.values)
    money_line_list.append(money_line.values)
    print(total_points.values)
    print("WHAHHASDKFJSDFLJSDFLKJSDFLKSJDL")
    print(money_line.values)
    print("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")
    if  total_points.values < money_line.values :
        over_under = 'UNDER'
    else:
        over_under = 'OVER'

    over_or_under_list.append(over_under)

over_or_under_list.reverse()
dataframe_schedule = pd.DataFrame({'OVER OR UNDER': over_or_under_list})
##dataframe_schedule2 = pd.DataFrame({'PACE PER GAME:': pace_per_game_list})
##dataframe_schedule2 = dataframe_schedule2.sort_index(axis=1 ,ascending=False)
##dataframe_schedule2 = dataframe_schedule2.iloc[::-1]
dataframe_schedule = dataframe_schedule.sort_index(axis=1 ,ascending=False)
dataframe_schedule = dataframe_schedule.iloc[::-1]
new_schedule_score = excel_data_df2.merge(dataframe_schedule, left_index=True, right_index=True)
##new_schedule_score2 = excel_data_df.merge(dataframe_schedule2, left_index=True, right_index=True)
stats_doc = ExcelWriter(time.strftime('Total_Points2_%Y_%m_%d.xlsx'), engine='openpyxl')
new_schedule_score.to_excel(stats_doc, sheet_name='Sheet1', index=False)
stats_doc.close()

excel_data_df2 = pd.read_excel(time.strftime('Total_Points2_%Y_%m_%d.xlsx'), sheet_name='Sheet1', engine='openpyxl')
##excel_data_df2['GAME POINTS WITH FORMULA:'].replace('', np.nan, inplace=True)
##excel_data_df2['GAME MONEY LINE:'].replace('', np.nan, inplace=True)
##excel_data_df2.dropna(subset=['GAME POINTS WITH FORMULA:'], inplace=True)
##excel_data_df2.dropna(subset=['GAME MONEY LINE:'], inplace=True)
stats_doc = ExcelWriter(time.strftime('Total_Points2_%Y_%m_%d.xlsx'), engine='openpyxl')
excel_data_df2.to_excel(stats_doc, sheet_name='Sheet1', index=False)
stats_doc.close()

excel_data_df4 = pd.read_excel(time.strftime('Total_Points2_%Y_%m_%d.xlsx'), sheet_name='Sheet1', engine='openpyxl')
excel_data_df4.to_sql(con=database_connection, name='mlb_v5_2024', if_exists='replace', index=False)
from shutil import copyfile

import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mlb_24"
)

mycursor7 = mydb.cursor()
sql7 = "ALTER TABLE mlb_v5_2024 ADD COLUMN `id` BIGINT(11) NOT NULL FIRST;"
mycursor7.execute(sql7)
mycursor7 = mydb.cursor()
sql7 = "ALTER TABLE mlb_v5_2024 MODIFY COLUMN `id` BIGINT(11) UNSIGNED PRIMARY KEY AUTO_INCREMENT;"
mycursor7.execute(sql7)