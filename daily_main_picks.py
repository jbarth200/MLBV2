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

mycursor.execute("SELECT `HOME TEAM:` FROM `mlb_v6` WHERE `HOME TEAM:` is NOT NULL")
myresult = mycursor.fetchall()
mycursor.execute("SELECT `OVER OR UNDER` FROM `mlb_v5` WHERE `HOME TEAM:` is NOT NULL")
myresult2 = mycursor.fetchall()
nun = myresult
mycursor.execute("SELECT `AWAY TEAM:` FROM `mlb_v6` WHERE `AWAY TEAM:` is NOT NULL")
myresult4 = mycursor.fetchall()
mycursor.execute("SELECT `OVER OR UNDER` FROM `mlb_v5` WHERE `AWAY TEAM:` is NOT NULL")
myresult5 = mycursor.fetchall()
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
home_field_hr_percent = []
home_field_xbases_percent = []
home_field_xruns_percent = []
home_pitcher_era = []
version2 = []
home_team_lose_percent = []
winpercenthome = []
winpercentaway = []
home_over_under_list = []
teamname2 = []
yahoo = 0
#Grabbing Home Team Win %
for team in myresult:
    data1 = team[yeet]

    data2 = "Win"
    values = (data1,data2)
    mycursor = mydb.cursor()
    totalwinshome = []
    sql3 = "SELECT `Win Or Lose:` FROM `previous_losses_mlb_v5_with_date_agg` WHERE `HOME TEAM:` = %s OR `HOME TEAM:` = %s AND `OVER OR UNDER` IS NOT NULL"
    mycursor.execute(sql3, values)
    home_win_percent = mycursor.fetchall()
    home_team_win_percent = []
    home_team_win_percent.append(home_win_percent)
    print(len(home_team_win_percent))
    print("above")
    print(home_team_win_percent)
    print("above2")
    for ending in home_team_win_percent:
        print(ending)
        print("otay")
        print(ending[1])
        cleanedup = str(ending)
        newstr = cleanedup.replace("',)", "")
        newstr2 = newstr.replace("('", "")
        print(newstr)
        print("otay2")
        print(newstr2)
        newstring = newstr2.split(",")
        print(newstring)
        print("DID WE?")
        print(newstring[0])
        print(len(newstring))
        for resultz in newstring:
            print("Thef what")
            print(resultz)
            print("What thef")
            if resultz == "[Win" or resultz == " Win" or resultz == " Win]":
                print(resultz)
                print("Okay we here")
                totalwinshome.append("win")

            print("Hell is this")
            print(totalwinshome)
            print(home_team_win_percent)

        print(totalwinshome)
        print("here it was")
        print(len(home_team_win_percent))
        percent = len(totalwinshome) / len(newstring)
        print(percent)
        print("Does This work")
        if percent > 0.625:
            winpercenthome.append(percent)
            home_over_under_list.append(myresult2[yahoo])
            version2.append("v5")
            teamname2.append(team)

    yahoo += 1

print(myresult)
print(winpercenthome)

version = []
yahoo2 = 0
teamname = []
away_over_under_list = []
for team in myresult4:
    data1 = team[yeet]
    data2 = "Win"
    print(team)
    print("Here is the team")
    values = (data1,data2)
    mycursor = mydb.cursor()
    totalwinsaway = []
    sql3 = "SELECT `Win Or Lose:` FROM `previous_losses_mlb_v5_with_date_agg` WHERE `AWAY TEAM:` = %s OR `AWAY TEAM:` = %s AND `OVER OR UNDER` IS NOT NULL"
    mycursor.execute(sql3, values)
    away_win_percent = mycursor.fetchall()
    away_team_win_percent = []
    away_team_win_percent.append(away_win_percent)
    print(len(away_team_win_percent))
    print("above")
    print(away_team_win_percent)
    print("above2")
    for ending in away_team_win_percent:
        print(ending)
        print("otay")
        print(ending[1])
        cleanedup2 = str(ending)
        newstr32 = cleanedup2.replace("',)", "")
        newstr22 = newstr32.replace("('", "")
        print(newstr)
        print("otay2")
        print(newstr2)
        newstring60 = newstr22.split(",")
        print(len(newstring60))
        print("Length of what we are diving")
        print(newstring)
        print("DID WE?")
        print(newstring[0])
        print(len(newstring))
        for resultz in newstring60:
            print("Thef what")
            print(resultz)
            print("What thef")
            if resultz == "[Win" or resultz == " Win" or resultz == " Win]":
                print(resultz)
                print("Okay we here")
                totalwinsaway.append("win")

            print("Hell is this")
            print(totalwinsaway)
            print(len(totalwinsaway))
            print(away_team_win_percent)

        print(totalwinsaway)
        print("here it was")
        print(len(away_team_win_percent))
        percent = len(totalwinsaway) / len(newstring60)
        print(percent)
        print("Does This work")
        if percent > 0.625:
            winpercentaway.append(percent)
            away_over_under_list.append(myresult5[yahoo2])
            version.append("v5")
            teamname.append(team)

    yahoo2 += 1




print(myresult)
print(winpercenthome)
print(myresult4)
print(winpercentaway)

hometeamwins = pd.DataFrame({'HOME TEAM:': teamname2, 'HOME TEAM WIN PERCENTAGE:':winpercenthome, 'FORMULA:': version2, 'OVER UNDER': home_over_under_list})
awayteamwins = pd.DataFrame({'AWAY TEAM:':teamname,'AWAY TEAM WIN PERCENTAGE:': winpercentaway, 'FORMULA:': version, 'OVER UNDER': away_over_under_list})



stats_doc = ExcelWriter('Top_Win_PercentHome.xlsx')
hometeamwins.to_excel(stats_doc, sheet_name='Sheet1', index=False)
stats_doc.close()

stats_doc = ExcelWriter('Top_Win_PercentAway.xlsx')
awayteamwins.to_excel(stats_doc, sheet_name='Sheet1', index=False)
stats_doc.close()


excel_data_df55 = pd.read_excel(yesterday.strftime('Top_Win_PercentHome.xlsx'), sheet_name='Sheet1', engine='openpyxl')
excel_data_df66 = pd.read_excel(yesterday.strftime('Top_Win_PercentAway.xlsx'), sheet_name='Sheet1', engine='openpyxl')
excel_data_df55.to_sql(con=database_connection, name='home_daily_picks', if_exists='append', index=False)
excel_data_df66.to_sql(con=database_connection, name='away_daily_picks', if_exists='append', index=False)
