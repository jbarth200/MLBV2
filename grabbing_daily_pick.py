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
#print(myresult)
#print(myresult4)
yeet = 0
home_team_wins = []
home_team = []
away_team_wins = []
#Grabbing Home Team Win/Lose Data
for team in myresult:
    data1 = "('" + team[yeet] + "',)"
    data2 = "('" + team[yeet] + "',)"
#    print(data1)
#    print(data2)
#    print("this should be the reawwww")
    home_team.append(team)
    values = (data1,data2)
    mycursor = mydb.cursor()

    sql2 = "SELECT `HOME WIN LOSE:` FROM `current_day_statsmlbv5_2022`  WHERE `HOME TEAM:` =" + "%s OR `AWAY TEAM:` = %s"
    #mycursor.execute(sql, values)
    #myresult = mycursor.fetchall()
    #pernn = myresult
    mycursor.execute(sql2, values)
    win_lose_home_team = mycursor.fetchall()
    #over_unders.append(myresult)
    #print(myresult)
#    print(win_lose_home_team)
#    print
    home_team_wins.append(win_lose_home_team)
#    print("WHAT THE FUCK")
#    print(type(home_team_wins))
newerlist = []
for item in home_team_wins:
#    print("Here is the item")
#    print(item)
    for item2 in item:
#        print('Here is item2')
#        print(item2)
        for item3 in item2:
#            print("Really item3???????")
#            print(item3)
            newerlist.append(item3)



#print('FULL LIST?')
#print(home_team_wins)
#print(newerlist)
#print("check here")
#print(newerlist[0])
newwerlist2 = [s.replace(""")]",""", """""") for s in newerlist]
newwerlist3 = [s.replace(""",),""", """""") for s in newwerlist2]
newwerlist4 = [s.replace("""(""", """""") for s in newwerlist3]
newwerlist5 = [s.replace(""",)""", """""") for s in newwerlist4]
newwerlist6 = [s.replace("""[""", """""") for s in newwerlist5]
newwerlist7 = [s.replace("""]""", """""") for s in newwerlist6]
newwerlist8 = [s.replace("""'""", """""") for s in newwerlist7]
#print(newwerlist8)
#print("HERE WE GO BABE")
#print(newwerlist8[1])
#newst = newwerlist4.split('"')
bestlist = []
for hey in newwerlist8:
    #print(hey)
    #print("WHat's it like?")
    hey.replace("""""", """,""")
    #print(type(hey))
    hey4 = hey.split()
    #print("Holy")
    bestlist.append(hey4)
    #print(hey4)

#print("IS THis REAL LIFE")
#print(bestlist)
teee = 0
winpercet = []
for tean in bestlist:
    #print("Here we are bitch")`
    print(teee)
    #print(tean)
    teee += 1
    winlist = []
    print("REFRESHER")
    for tean2 in tean:

        #print(tean2)
        #print("CUNT")

        if tean2 == "Win":
            print("DAMNit it fuCKNG woRKingED")
            winlist.append(tean2)

        else:
            print("IT REALLY FUCKING DID WORK ")

    perc = len(winlist) / len(tean) * 100
    print(len(winlist))
    print(len(tean))
    print('Does this not add up?')
    winpercet.append(perc)
    print(teee)
    teee += 1

print(winpercet)
print("No way this worked")
away_team_wins = []
away_team = []
for team in myresult4:
    data1 = "('" + team[yeet] + "',)"
    data2 = "('" + team[yeet] + "',)"
#    print(data1)
#    print(data2)
#    print("this should be the reawwww")
    away_team.append(team)
    values = (data1,data2)
    mycursor = mydb.cursor()

    sql2 = "SELECT `AWAY WIN LOSE:` FROM `current_day_statsmlbv5_2022`  WHERE `HOME TEAM:` =" + "%s OR `AWAY TEAM:` = %s"
    #mycursor.execute(sql, values)
    #myresult = mycursor.fetchall()
    #pernn = myresult
    mycursor.execute(sql2, values)
    win_lose_home_team = mycursor.fetchall()
    #over_unders.append(myresult)
    #print(myresult)
#    print(win_lose_home_team)
#    print
    away_team_wins.append(win_lose_home_team)
#    print("WHAT THE FUCK")
#    print(type(home_team_wins))
newerlist = []
for item in away_team_wins:
#    print("Here is the item")
#    print(item)
    for item2 in item:
#        print('Here is item2')
#        print(item2)
        for item3 in item2:
#            print("Really item3???????")
#            print(item3)
            newerlist.append(item3)



#print('FULL LIST?')
#print(home_team_wins)
#print(newerlist)
#print("check here")
#print(newerlist[0])
newwerlist2 = [s.replace(""")]",""", """""") for s in newerlist]
newwerlist3 = [s.replace(""",),""", """""") for s in newwerlist2]
newwerlist4 = [s.replace("""(""", """""") for s in newwerlist3]
newwerlist5 = [s.replace(""",)""", """""") for s in newwerlist4]
newwerlist6 = [s.replace("""[""", """""") for s in newwerlist5]
newwerlist7 = [s.replace("""]""", """""") for s in newwerlist6]
newwerlist8 = [s.replace("""'""", """""") for s in newwerlist7]
#print(newwerlist8)
#print("HERE WE GO BABE")
#print(newwerlist8[1])
#newst = newwerlist4.split('"')
bestlist = []
for hey in newwerlist8:
    #print(hey)
    #print("WHat's it like?")
    hey.replace("""""", """,""")
    #print(type(hey))
    hey4 = hey.split()
    #print("Holy")
    bestlist.append(hey4)
    #print(hey4)

#print("IS THis REAL LIFE")
#print(bestlist)
teee = 0
winpercetaway = []
for tean in bestlist:
    #print("Here we are bitch")`
    print(teee)
    #print(tean)
    teee += 1
    winlist = []
    print("REFRESHER")
    for tean2 in tean:

        #print(tean2)
        #print("CUNT")

        if tean2 == "Win":
            print("DAMNit it fuCKNG woRKingED")
            winlist.append(tean2)

        else:
            print("IT REALLY FUCKING DID WORK ")

    perc = len(winlist) / len(tean) * 100
    print(len(winlist))
    print(len(tean))
    print('Does this not add up?')
    winpercetaway.append(perc)
    print(teee)
    teee += 1


print(winpercet)
print(home_team)
print(winpercetaway)
print(away_team)
print(len(winpercet))
print(len(winpercetaway))
print("No way this worked AWAY")


dataframe_schedule = pd.DataFrame({'HOME TEAM:': home_team, 'AWAY TEAM:': away_team, 'HOME WIN PERCENT': winpercet, 'AWAY WIN PERCENT:': winpercetaway})
stats_doc = ExcelWriter(yesterday.strftime('Win_Percent.xlsx'), engine='openpyxl')
dataframe_schedule.to_excel(stats_doc, sheet_name='Sheet1', index=False)
stats_doc.close()

excel_data_df4 = pd.read_excel(yesterday.strftime('Win_Percent.xlsx'), sheet_name='Sheet1', engine='openpyxl')
excel_data_df4.to_sql(con=database_connection, name='win_precent_mlbv5', if_exists='replace', index=False)


mycursor = mydb.cursor()

mycursor.execute("SELECT `HOME TEAM:` FROM `win_precent_mlbv5` WHERE `HOME WIN PERCENT` > 58 OR `AWAY WIN PERCENT:` > 58")

myresult = mycursor.fetchall()
game_pick = myresult

print(game_pick)
yeet= 0


newerlist33 = []

for item in game_pick:
#    print("Here is the item")
#    print(item)
    for item2 in item:
#        print('Here is item2')
#        print(item2)
         newerlist33.append(item2)




#print('FULL LIST?')
#print(home_team_wins)
#print(newerlist)
#print("check here")
#print(newerlist[0])
newwerlist24 = [s.replace(""")]",""", """""") for s in newerlist33]
newwerlist34 = [s.replace(""",),""", """""") for s in newwerlist24]
newwerlist44 = [s.replace("""(""", """""") for s in newwerlist34]
newwerlist54 = [s.replace(""",)""", """""") for s in newwerlist44]
newwerlist64 = [s.replace("""[""", """""") for s in newwerlist54]
newwerlist74 = [s.replace("""]""", """""") for s in newwerlist64]
newwerlist84 = [s.replace("""'""", """""") for s in newwerlist74]

yeet = 0
final_game_picks_home_team = []
final_game_picks_away_team = []
final_game_picks_game_points = []
final_game_picks_money_line = []
#Grabbing Home Team Over Under Past 5
for team in newwerlist84:
    data1 = team
    data2 = team
    values = (data1,data2)
    print(values)
    print("HERE IS THE TEAM ABOVE")
    mycursor = mydb.cursor()
    sql = "SELECT `HOME TEAM:` FROM `mlb_v5` WHERE `HOME TEAM:` = %s OR `AWAY TEAM:` = %s"
    sql2 = "SELECT `AWAY TEAM:` FROM `mlb_v5` WHERE `HOME TEAM:` = %s OR `AWAY TEAM:` = %s"
    sql3 = "SELECT `GAME POINTS WITH FORMULA:` FROM `mlb_v5` WHERE `HOME TEAM:` = %s OR `AWAY TEAM:` = %s"
    sql4 = "SELECT `MONEY LINE:` FROM `mlb_v5` WHERE `HOME TEAM:` = %s OR `AWAY TEAM:` = %s"
    mycursor.execute(sql, values)
    myresult = mycursor.fetchall()
    mycursor.execute(sql2, values)
    myresult2 = mycursor.fetchall()
    mycursor.execute(sql3, values)
    myresult3 = mycursor.fetchall()
    mycursor.execute(sql4, values)
    myresult4 = mycursor.fetchall()
    #mycursor.execute(sql2, values)
    #win_lose_home_team = mycursor.fetchall()
    #over_unders.append(myresult[-5:])
    print(myresult)
    #print(win_lose_home_team)
    #home_team_wins.append(win_lose_home_team)
    #print("WHAT THE FUCK")
    final_game_picks_home_team.append(myresult)
    final_game_picks_away_team.append(myresult2)
    final_game_picks_game_points.append(myresult3)
    final_game_picks_money_line.append(myresult4)

print(final_game_picks_home_team)
print(final_game_picks_away_team)
print(final_game_picks_game_points)
print(final_game_picks_money_line)
print("HEre it is!!!")
version = []
for team in final_game_picks_home_team:
    version.append("V4")


dataframe_schedule = pd.DataFrame({'HOME TEAM:': final_game_picks_home_team, 'AWAY TEAM:': final_game_picks_away_team, 'GAME POINTS:': final_game_picks_game_points, 'MONEY LINE:': final_game_picks_money_line, 'FORMULA': version})
dataframe_schedule = dataframe_schedule.sort_index(axis=1 ,ascending=True)


stats_doc = ExcelWriter(yesterday.strftime('finalfinal_mlbv5picks.xlsx'), engine='openpyxl')
dataframe_schedule.to_excel(stats_doc, sheet_name='Sheet1', index=False)
stats_doc.close()

excel_data_df4 = pd.read_excel(yesterday.strftime('finalfinal_mlbv5picks.xlsx'), sheet_name='Sheet1', engine='openpyxl')
excel_data_df4 = excel_data_df4.replace({'\\[':''}, regex=True)
excel_data_df4 = excel_data_df4.replace({'\\]':''}, regex=True)
excel_data_df4 = excel_data_df4.replace({"\\'":''}, regex=True)
excel_data_df4 = excel_data_df4.replace({'\\"':''}, regex=True)
excel_data_df4 = excel_data_df4.replace({'\\(':''}, regex=True)
excel_data_df4 = excel_data_df4.replace({'\\)':''}, regex=True)
excel_data_df4 = excel_data_df4.replace({'\\,':''}, regex=True)
stats_doc = ExcelWriter('finalfinal_mlbv5picks.xlsx', engine='openpyxl')
excel_data_df4.to_excel(stats_doc, sheet_name='Sheet1', index=False)
stats_doc.close()

excel_data_df5 = pd.read_excel(yesterday.strftime('finalfinal_mlbv5picks.xlsx'), sheet_name='Sheet1', engine='openpyxl')
excel_data_df5.to_sql(con=database_connection, name='daily_picks_mlb5', if_exists='replace', index=False)
excel_data_df5.to_sql(con=database_connection, name='daily_picks_mlb', if_exists='append', index=False)