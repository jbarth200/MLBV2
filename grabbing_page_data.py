import mysql.connector
import time

import pandas as pd
from datetime import date, timedelta
from pandas import ExcelWriter
yesterday = date.today() - timedelta(+1)
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mlb_24"
)
import sqlalchemy

database_username = 'root'
database_password = ''
database_ip = 'localhost'
database_name = 'mlb_24'
database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                               format(database_username, database_password,
                                                    database_ip, database_name))
mycursor = mydb.cursor()

mycursor.execute("SELECT `HOME TEAM:` FROM `mlb_v5` WHERE `HOME TEAM:` is NOT NULL")

myresult = mycursor.fetchall()
nun = myresult
mycursor.execute("SELECT `AWAY TEAM:` FROM `mlb_v5` WHERE `AWAY TEAM:` is NOT NULL")
myresult4 = mycursor.fetchall()
numn = myresult4
print(myresult)
print(myresult4)
zip_object = zip(myresult, myresult4, myresult, myresult4)
yeet = 0
awayuyu = []
homeuyu = []
over_unders = []
over_unders2 = []
kt = "Atlanta"
temp1 = "Miami"
temp2 = "Toronto"
home_team_wins = []
away_team_wins = []
home_home_team_wins = []
away_home_team_wins = []
home_away_team_wins = []
away_away_team_wins = []
home_total_points = []
home_home_points = []
home_away_points = []
away_home_points = []
away_away_points = []
home_home_overunder = []
home_away_overunder = []
away_home_overunder = []
away_away_overunder = []
home_over_under = []
away_over_under = []
home_team_win_0 = []
home_team_win_1 = []
home_team_win_2 = []
home_team_win_3 = []
home_team_win_4 = []
home_team_win_5 = []
home_team_win_6 = []
home_team_pitchers = []
#Grabbing Home Team Over Under Past 5
for team in myresult:
    data1 = team[yeet]
    data2 = team[yeet]
    values = (data1,data2)
    mycursor = mydb.cursor()
    sql = "SELECT `ACTUAL OVER UNDER RESULT:` FROM `previous_losses_mlbv5_2021_with_date_agg` WHERE `HOME TEAM:` = %s OR `AWAY TEAM:` = %s"
    sql2 = "SELECT `Win Or Lose:` FROM `previous_losses_mlbv5_2021_with_date_agg` WHERE `HOME TEAM:` = %s OR `AWAY TEAM:` = %s"
    sql3 = "SELECT `Win Or Lose:` FROM `previous_losses_mlbv5_2021_with_date_agg` WHERE `HOME TEAM:` = %s OR `HOME TEAM:` = %s"
    sql4 = "SELECT `Win Or Lose:` FROM `previous_losses_mlbv5_2021_with_date_agg` WHERE `AWAY TEAM:` = %s OR `AWAY TEAM:` = %s"
    sql00 = "SELECT `Win Or Lose:` FROM previous_losses_mlbv5_2021_with_date_agg WHERE weekday(`DATE:`) = '0' AND (`HOME TEAM:` = %s OR `AWAY TEAM:` = %s)"
    sql000 = "SELECT `Win Or Lose:` FROM previous_losses_mlbv5_2021_with_date_agg WHERE weekday(`DATE:`) = '1' AND (`HOME TEAM:` = %s OR `AWAY TEAM:` = %s)"
    sql01 = "SELECT `Win Or Lose:` FROM previous_losses_mlbv5_2021_with_date_agg WHERE weekday(`DATE:`) = '1' AND (`HOME TEAM:` = %s OR `AWAY TEAM:` = %s)"
    sql02 = "SELECT `Win Or Lose:` FROM previous_losses_mlbv5_2021_with_date_agg WHERE weekday(`DATE:`) = '2' AND (`HOME TEAM:` = %s OR `AWAY TEAM:` = %s)"
    sql03 = "SELECT `Win Or Lose:` FROM previous_losses_mlbv5_2021_with_date_agg WHERE weekday(`DATE:`) = '3' AND (`HOME TEAM:` = %s OR `AWAY TEAM:` = %s)"
    sql04 = "SELECT `Win Or Lose:` FROM previous_losses_mlbv5_2021_with_date_agg WHERE weekday(`DATE:`) = '4' AND (`HOME TEAM:` = %s OR `AWAY TEAM:` = %s)"
    sql05 = "SELECT `Win Or Lose:` FROM previous_losses_mlbv5_2021_with_date_agg WHERE weekday(`DATE:`) = '5' AND (`HOME TEAM:` = %s OR `AWAY TEAM:` = %s)"
    sql06 = "SELECT `Win Or Lose:` FROM previous_losses_mlbv5_2021_with_date_agg WHERE weekday(`DATE:`) = '6' AND (`HOME TEAM:` = %s OR `AWAY TEAM:` = %s)"
    sql07 = "SELECT `HOME PITCHER:` FROM `mlb_starting_pitchers` WHERE `HOME TEAM:` = %s OR `HOME TEAM:` = %s"

    mycursor.execute(sql, values)
    myresult = mycursor.fetchall()
    pernn = myresult[:5]
    mycursor.execute(sql2, values)
    win_lose_home_team = mycursor.fetchall()
    over_unders.append(myresult[-5:])
    home_over_under.append(myresult)
    mycursor.execute(sql3, values)
    home_win_lose_home_team = mycursor.fetchall()
    mycursor.execute(sql4, values)
    away_win_lose_home_team = mycursor.fetchall()
    mycursor.execute(sql00, values, multi=True)
    home_team_win_day_0 = mycursor.fetchall()
    home_team_win_0.append(home_team_win_day_0)
    mycursor.execute(sql01, values)
    home_team_win_day_1 = mycursor.fetchall()
    home_team_win_1.append(home_team_win_day_1)
    mycursor.execute(sql02, values)
    home_team_win_day_2 = mycursor.fetchall()
    home_team_win_2.append(home_team_win_day_2)
    mycursor.execute(sql03, values)
    home_team_win_day_3 = mycursor.fetchall()
    home_team_win_3.append(home_team_win_day_3)
    mycursor.execute(sql04, values)
    home_team_win_day_4 = mycursor.fetchall()
    home_team_win_4.append(home_team_win_day_4)
    mycursor.execute(sql05, values)
    home_team_win_day_5 = mycursor.fetchall()
    home_team_win_5.append(home_team_win_day_5)
    mycursor.execute(sql06, values)
    home_team_win_day_6 = mycursor.fetchall()
    home_team_win_6.append(home_team_win_day_6)
    mycursor.execute(sql07, values)
    home_team_pitcher = mycursor.fetchall()
    home_team_pitchers.append(home_team_pitcher)
    print("WHAT IS GOIUGG ION")
    print(myresult)
    print(win_lose_home_team)
    home_team_wins.append(win_lose_home_team)
    home_home_team_wins.append(home_win_lose_home_team)
    away_home_team_wins.append(away_win_lose_home_team)
    print("WHAT THE FUCK")
    sql5 = "SELECT `HOME TEAM POINTS:` FROM `previous_losses_mlbv5_2021_with_date_agg` WHERE `HOME TEAM:` = %s OR `HOME TEAM:` = %s"
    mycursor.execute(sql5, values)
    myresult = mycursor.fetchall()
    home_home_points.append(myresult[-5:])
    sql6 = "SELECT `AWAY TEAM POINTS:` FROM `previous_losses_mlbv5_2021_with_date_agg` WHERE `AWAY TEAM:` = %s OR `AWAY TEAM:` = %s"
    mycursor.execute(sql6, values)
    myresult = mycursor.fetchall()
    home_away_points.append(myresult[-5:])



    sql7 = "SELECT `ACTUAL OVER UNDER RESULT:` FROM `previous_losses_mlbv5_2021_with_date_agg` WHERE `HOME TEAM:` = %s OR `HOME TEAM:` = %s"
    mycursor.execute(sql7, values)
    myresult = mycursor.fetchall()
    home_home_overunder.append(myresult)
    sql8 = "SELECT `ACTUAL OVER UNDER RESULT:` FROM `previous_losses_mlbv5_2021_with_date_agg` WHERE `AWAY TEAM:` = %s OR `AWAY TEAM:` = %s"
    mycursor.execute(sql8, values)
    myresult = mycursor.fetchall()
    home_away_overunder.append(myresult)

print("GET IT")
print(home_home_points)
print(home_away_points)
away_team_win_0 = []
away_team_win_1 = []
away_team_win_2 = []
away_team_win_3 = []
away_team_win_4 = []
away_team_win_5 = []
away_team_win_6 = []
away_team_pitchers = []
#Grabbing Away Team Over Under Past 5
for team in myresult4:
    data1 = team[yeet]
    data2 = team[yeet]
    values = (data1,data2)
    mycursor = mydb.cursor()
    sql = "SELECT `ACTUAL OVER UNDER RESULT:` FROM `previous_losses_mlbv5_2021_with_date_agg` WHERE `HOME TEAM:` = %s OR `AWAY TEAM:` = %s"
    sql2 = "SELECT `Win Or Lose:` FROM `previous_losses_mlbv5_2021_with_date_agg` WHERE `HOME TEAM:` = %s OR `AWAY TEAM:` = %s"
    sql00 = "SELECT `Win Or Lose:` FROM previous_losses_mlbv5_2021_with_date_agg WHERE weekday(`DATE:`) = '0' AND (`HOME TEAM:` = %s OR `AWAY TEAM:` = %s)"
    sql000 = "SELECT `Win Or Lose:` FROM previous_losses_mlbv5_2021_with_date_agg WHERE weekday(`DATE:`) = '1' AND (`HOME TEAM:` = %s OR `AWAY TEAM:` = %s)"
    sql01 = "SELECT `Win Or Lose:` FROM previous_losses_mlbv5_2021_with_date_agg WHERE weekday(`DATE:`) = '1' AND (`HOME TEAM:` = %s OR `AWAY TEAM:` = %s)"
    sql02 = "SELECT `Win Or Lose:` FROM previous_losses_mlbv5_2021_with_date_agg WHERE weekday(`DATE:`) = '2' AND (`HOME TEAM:` = %s OR `AWAY TEAM:` = %s)"
    sql03 = "SELECT `Win Or Lose:` FROM previous_losses_mlbv5_2021_with_date_agg WHERE weekday(`DATE:`) = '3' AND (`HOME TEAM:` = %s OR `AWAY TEAM:` = %s)"
    sql04 = "SELECT `Win Or Lose:` FROM previous_losses_mlbv5_2021_with_date_agg WHERE weekday(`DATE:`) = '4' AND (`HOME TEAM:` = %s OR `AWAY TEAM:` = %s)"
    sql05 = "SELECT `Win Or Lose:` FROM previous_losses_mlbv5_2021_with_date_agg WHERE weekday(`DATE:`) = '5' AND (`HOME TEAM:` = %s OR `AWAY TEAM:` = %s)"
    sql06 = "SELECT `Win Or Lose:` FROM previous_losses_mlbv5_2021_with_date_agg WHERE weekday(`DATE:`) = '6' AND (`HOME TEAM:` = %s OR `AWAY TEAM:` = %s)"
    sql3 = "SELECT `Win Or Lose:` FROM `previous_losses_mlbv5_2021_with_date_agg` WHERE `HOME TEAM:` = %s OR `HOME TEAM:` = %s"
    sql4 = "SELECT `Win Or Lose:` FROM `previous_losses_mlbv5_2021_with_date_agg` WHERE `AWAY TEAM:` = %s OR `AWAY TEAM:` = %s"
    sql07 = "SELECT `AWAY PITCHER:` FROM `mlb_starting_pitchers` WHERE `AWAY TEAM:` = %s OR `AWAY TEAM:` = %s"
    mycursor.execute(sql, values)
    myresult3 = mycursor.fetchall()
    mycursor.execute(sql2, values)
    win_lose_away_team = mycursor.fetchall()
    over_unders2.append(myresult3[-5:])
    away_over_under.append(myresult3)
    mycursor.execute(sql3, values)
    home_win_lose_home_team = mycursor.fetchall()
    mycursor.execute(sql4, values)
    away_win_lose_home_team = mycursor.fetchall()
    mycursor.execute(sql00, values)
    away_team_win_day_0 = mycursor.fetchall()
    away_team_win_0.append(away_team_win_day_0)
    mycursor.execute(sql01, values)
    away_team_win_day_1 = mycursor.fetchall()
    away_team_win_1.append(away_team_win_day_1)
    mycursor.execute(sql02, values)
    away_team_win_day_2 = mycursor.fetchall()
    away_team_win_2.append(away_team_win_day_2)
    mycursor.execute(sql03, values)
    away_team_win_day_3 = mycursor.fetchall()
    away_team_win_3.append(away_team_win_day_3)
    mycursor.execute(sql04, values)
    away_team_win_day_4 = mycursor.fetchall()
    away_team_win_4.append(away_team_win_day_4)
    mycursor.execute(sql05, values)
    away_team_win_day_5 = mycursor.fetchall()
    away_team_win_5.append(away_team_win_day_5)
    mycursor.execute(sql06, values)
    away_team_win_day_6 = mycursor.fetchall()
    away_team_win_6.append(away_team_win_day_6)
    mycursor.execute(sql07, values)
    away_team_pitcher = mycursor.fetchall()
    away_team_pitchers.append(away_team_pitcher)
    print(myresult)
    away_team_wins.append(win_lose_away_team)
    home_away_team_wins.append(home_win_lose_home_team)
    away_away_team_wins.append(away_win_lose_home_team)

    print("What the hell")
    sql5 = "SELECT `HOME TEAM POINTS:` FROM `previous_losses_mlbv5_2021_with_date_agg` WHERE `HOME TEAM:` = %s OR `HOME TEAM:` = %s"
    mycursor.execute(sql5, values)
    myresult = mycursor.fetchall()
    away_home_points.append(myresult[-5:])
    sql6 = "SELECT `AWAY TEAM POINTS:` FROM `previous_losses_mlbv5_2021_with_date_agg` WHERE `AWAY TEAM:` = %s OR `AWAY TEAM:` = %s"
    mycursor.execute(sql6, values)
    myresult = mycursor.fetchall()
    away_away_points.append(myresult[-5:])

    sql7 = "SELECT `ACTUAL OVER UNDER RESULT:` FROM `previous_losses_mlbv5_2021_with_date_agg` WHERE `HOME TEAM:` = %s OR `HOME TEAM:` = %s"
    mycursor.execute(sql7, values)
    myresult = mycursor.fetchall()
    away_home_overunder.append(myresult)
    sql8 = "SELECT `ACTUAL OVER UNDER RESULT:` FROM `previous_losses_mlbv5_2021_with_date_agg` WHERE `AWAY TEAM:` = %s OR `AWAY TEAM:` = %s"
    mycursor.execute(sql8, values)
    myresult = mycursor.fetchall()
    away_away_overunder.append(myresult)

print("Got it Here")
print(away_home_points)
print(away_away_points)


print("Well here it is")
print(over_unders)
print(over_unders2)




between_teams = []
#Grabbing Over Under Results From Previous Games Of Teams Going Against Eachother
for element1, element2, element3, element4 in zip_object:
    data1 = element1[yeet]
    data2 = element2[yeet]
    data3 = element3[yeet]
    data4 = element4[yeet]
    print("HEre are the teams?")
    print(element1)
    print(element2)
    print(element3)
    print(element4)
    values5 = (data1, data2, data4, data3)
    mycursor5 = mydb.cursor()
    sql5 = "SELECT `ACTUAL OVER UNDER RESULT:` FROM `previous_losses_mlbv5_2021_with_date_agg` WHERE `HOME TEAM:` = %s AND `AWAY TEAM:` = %s OR `HOME TEAM:` = %s AND `AWAY TEAM:` = %s"
    mycursor5.execute(sql5, values5)
    myresult5 = mycursor5.fetchall()
    between_teams.append(myresult5)
    print("Fuck yeah")
    print(myresult5)
print("finaly between teams")
print(between_teams)


print(len(over_unders))
print(len(over_unders2))
print(len(between_teams))

print(len(away_team_win_0))
print(len(away_team_win_1))
print(len(away_team_win_2))
print(len(away_team_win_3))
print(len(away_team_win_4))
print(len(away_team_win_5))
print(len(away_team_win_6))

dataframe_schedule = pd.DataFrame({'HOME TEAM:': nun, 'AWAY TEAM:': numn, 'HOME TEAM OVER UNDER:': over_unders, 'AWAY TEAM OVER UNDER:': over_unders2, 'OVER UNDER BETWEEN TEAMS:': between_teams, 'HOME WIN LOSE:': home_team_wins, 'AWAY WIN LOSE:': away_team_wins, 'HOME TEAM HOME WINS': home_home_team_wins, 'HOME TEAM AWAY WINS': away_home_team_wins, 'AWAY TEAM HOME WINS': home_away_team_wins, 'AWAY TEAM AWAY WINS': away_away_team_wins, 'HOME AT HOME POINTS': home_home_points, 'HOME AT AWAY POINTS': home_away_points, 'AWAY AT HOME POINTS': away_home_points, 'AWAY AT AWAY POINTS': away_away_points, 'HOME AT HOME OVER UNDER': home_home_overunder, 'HOME AT AWAY OVER UNDER': home_away_overunder, 'AWAY AT HOME OVER UNDER': away_home_overunder, 'AWAY AT AWAY OVER UNDER': away_away_overunder, 'HOME TOTAL OVER UNDER': home_over_under, 'AWAY TOTAL OVER UNDER': away_over_under, 'home_team_win_0': home_team_win_0, 'home_team_win_1': home_team_win_1, 'home_team_win_2': home_team_win_2, 'home_team_win_3': home_team_win_3, 'home_team_win_4': home_team_win_4, 'home_team_win_5': home_team_win_5, 'home_team_win_6': home_team_win_6, 'away_team_win_0': away_team_win_0, 'away_team_win_1': away_team_win_1, 'away_team_win_2': away_team_win_2, 'away_team_win_3': away_team_win_3, 'away_team_win_4': away_team_win_4, 'away_team_win_5': away_team_win_5, 'away_team_win_6': away_team_win_6, 'HOME TEAM PITCHERS:': home_team_pitchers, 'AWAY TEAM PITCHERS:': away_team_pitchers})
dataframe_schedule = dataframe_schedule.sort_index(axis=1 ,ascending=True)


stats_doc = ExcelWriter(yesterday.strftime('Current_Day_Over_Under.xlsx'), engine='openpyxl')
dataframe_schedule.to_excel(stats_doc, sheet_name='Sheet1', index=False)
stats_doc.close()

excel_data_df4 = pd.read_excel(yesterday.strftime('Current_Day_Over_Under.xlsx'), sheet_name='Sheet1', engine='openpyxl')
excel_data_df4.to_sql(con=database_connection, name='current_day_statsmlbv5', if_exists='replace', index=False)



