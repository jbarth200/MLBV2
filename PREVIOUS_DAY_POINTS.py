import requests
import time
import csv
import locale
import pandas as pd
import json
from lxml import etree

from lxml import html
from io import StringIO
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np


try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

from datetime import date, timedelta

yesterday = date.today() - timedelta(+1)

#################################################################################

# Set explicit HTMLParser
parser = etree.HTMLParser()

page = requests.get(yesterday.strftime(('https://www.vsin.com/matchups/mlb/?y=%Y&m=%m&d=%d&c=DIV1&p=y')))
time.sleep(5)
# Decode the page content from bytes to string
html = page.content.decode("utf-8")

# Create your etree with a StringIO object which functions similarly
# to a fileHandler
tree = etree.parse(StringIO(html), parser=parser)
## Creating var for page path MAYBE?!?!?!
refs = tree.xpath('//*[@id="main-content"]/div[2]/div[2]/div[2]/text()')

print(len(refs))
## Creating length of teams listed
testssss = tree.xpath('//*[@id="main-content"]/div[2]/div[2]/text()')
print(len(testssss))

##Creating our start for iteration
yahoo = 0

##Creating our blank lists

money_line_list = list()
game_status_list = list()
away_team_list = list()
home_team_list = list()
away_team_score_list = list()
home_team_score_list = []


for teams in refs:
    yahoo += 1
    print(yahoo)
    #away_team = tree.xpath('/html/body/form/div[2]/div[2]/div/div/main/div[3]/div[2]/div[$d1_page1_point_margin_list_var]/table/thead[1]/tr/th[1]/a/span[1]/text()',d1_page1_point_margin_list_var=yahoo)
    away_team = tree.xpath('/html/body/form/div[2]/div[2]/div/div/main/div[2]/div[2]/div[2]/div[$d1_page1_point_margin_list_var]/table[1]/thead/tr/th[1]/a/span[1]/text()',d1_page1_point_margin_list_var=yahoo)
    home_team = tree.xpath('/html/body/form/div[2]/div[2]/div/div/main/div[2]/div[2]/div[2]/div[$d1_page1_point_margin_list_var]/table[1]/thead/tr/th[1]/a/span[2]/text()',d1_page1_point_margin_list_var=yahoo)
    away_team_score = tree.xpath('/html/body/form/div[2]/div[2]/div/div/main/div[2]/div[2]/div[2]/div[$d1_page1_point_margin_list_var]/table[1]/tbody/tr[1]/td/div/div[2]/div[1]/text()[1]',d1_page1_point_margin_list_var=yahoo)

    home_team_score = tree.xpath('/html/body/form/div[2]/div[2]/div/div/main/div[2]/div[2]/div[2]/div[$d1_page1_point_margin_list_var]/table[1]/tbody/tr[1]/td/div/div[2]/div[1]/text()[2]',d1_page1_point_margin_list_var=yahoo)
    print(away_team_score)
    print(home_team_score)
    away_team_score_list.append(away_team_score)
    home_team_score_list.append(home_team_score)
    ## print(team_all)
   ## team_list.append(team_all)
   ## print(refs2)
   ## turn_over_per_game.append(refs2)
    away_team_list.append(away_team)
    home_team_list.append(home_team)



print(away_team_list)
print(home_team_list)


away_team_list.reverse()
home_team_list.reverse()
away_team_score_list.reverse()
home_team_score_list.reverse()

new_schedule_total_score = pd.DataFrame({'HOME TEAM:':home_team_list, 'AWAY TEAM:':away_team_list, 'HOME TEAM POINTS:': home_team_score_list, 'AWAY TEAM POINTS:': away_team_score_list})
print(new_schedule_total_score)



stats_doc = ExcelWriter('Previous With Points.xlsx')
new_schedule_total_score.to_excel(stats_doc, sheet_name='Sheet1', index=False)
stats_doc.close()


new_schedule_total_score = pd.read_excel('Previous With Points.xlsx', sheet_name='Sheet1', engine='openpyxl')
new_schedule_total_score = new_schedule_total_score.replace({'\\"': ''}, regex=True)
new_schedule_total_score = new_schedule_total_score.replace({'\\]': ''}, regex=True)
new_schedule_total_score = new_schedule_total_score.replace({'\\[': ''}, regex=True)
new_schedule_total_score = new_schedule_total_score.replace({"\\'": ''}, regex=True)
df2 = new_schedule_total_score.apply(lambda x: pd.to_numeric(x.astype(str).str.replace(',',''), errors='coerce'))
df3 = df2.fillna(new_schedule_total_score)
stats_doc = ExcelWriter('Previous With Points.xlsx', engine='openpyxl')
df3.to_excel(stats_doc, sheet_name='Sheet1', index=False)
stats_doc.close()



data_frame_final_total = pd.read_excel('Previous With Points.xlsx', sheet_name='Sheet1', engine='openpyxl')



print(data_frame_final_total)

home_points = list()
away_points = list()
total_points = list()

for teams in refs:
    yahoo -= 1
    searching_home_points_previous_day = data_frame_final_total.iloc[yahoo, 2]
    print(searching_home_points_previous_day)
    home_points.append(searching_home_points_previous_day)
    searching_away_points_previous_day = data_frame_final_total.iloc[yahoo, 3]
    print(searching_away_points_previous_day)
    away_points.append(searching_away_points_previous_day)
    total = searching_home_points_previous_day + searching_away_points_previous_day
    print(total)
    total_points.append(total)
    print("RIGHTHEREEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")

total_points.reverse()

dataframe_nba_total_scores = pd.DataFrame({'ACTUAL GAME POINTS:': total_points})

new_schedule_total_score = data_frame_final_total.merge(dataframe_nba_total_scores, left_index=True, right_index=True)


stats_doc = ExcelWriter('Previous With Points.xlsx', engine='openpyxl')
new_schedule_total_score.to_excel(stats_doc, sheet_name='Sheet1', index=False)
stats_doc.close()

new_schedule_total_score = pd.read_excel('Previous With Points.xlsx', sheet_name='Sheet1', engine='openpyxl')
new_schedule_total_score = new_schedule_total_score.replace({'Miami Marlins':'Miami'}, regex=True)
new_schedule_total_score = new_schedule_total_score.replace({'Atlanta Braves':'Atlanta'}, regex=True)
new_schedule_total_score = new_schedule_total_score.replace({'Washington Nationals':'Washington'}, regex=True)
new_schedule_total_score = new_schedule_total_score.replace({'St. Louis Cardinals':'St. Louis'}, regex=True)
new_schedule_total_score = new_schedule_total_score.replace({'Cleveland Guardians':'Cleveland'}, regex=True)
new_schedule_total_score = new_schedule_total_score.replace({'Chicago White Sox':'Chi. White Sox'}, regex=True)
new_schedule_total_score = new_schedule_total_score.replace({'Los Angeles Angels':'L.A. Angels'}, regex=True)
new_schedule_total_score = new_schedule_total_score.replace({'Kansas City Royals':'Kansas City'}, regex=True)
new_schedule_total_score = new_schedule_total_score.replace({'Detroit Tigers':'Detroit'}, regex=True)
new_schedule_total_score = new_schedule_total_score.replace({'Houston Astros':'Houston'}, regex=True)
new_schedule_total_score = new_schedule_total_score.replace({'Oakland Athletics':'Oakland'}, regex=True)
new_schedule_total_score = new_schedule_total_score.replace({'Arizona Diamondbacks':"Arizona"}, regex=True)
new_schedule_total_score = new_schedule_total_score.replace({'Cincinnati Reds':"Cincinnati"}, regex=True)
new_schedule_total_score = new_schedule_total_score.replace({'San Francisco Giants':"San Francisco"}, regex=True)
new_schedule_total_score = new_schedule_total_score.replace({'San Diego Padres':"San Diego"}, regex=True)
new_schedule_total_score = new_schedule_total_score.replace({'Pittsburgh Pirates':"Pittsburgh"}, regex=True)
new_schedule_total_score = new_schedule_total_score.replace({'New York Yankees':"N.Y. Yankees"}, regex=True)

new_schedule_total_score = new_schedule_total_score.replace({'Minnesota Wild':"Minnesota"}, regex=True)
new_schedule_total_score = new_schedule_total_score.replace({'Toronto Blue Jays':"Toronto"}, regex=True)
new_schedule_total_score = new_schedule_total_score.replace({'Texas Rangers':"Texas"}, regex=True)
new_schedule_total_score = new_schedule_total_score.replace({'Tampa Bay Rays':"Tampa Bay"}, regex=True)
new_schedule_total_score = new_schedule_total_score.replace({'Chicago Cubs':"Chi. Cubs"}, regex=True)
new_schedule_total_score = new_schedule_total_score.replace({'Milwaukee Brewers':"Milwaukee"}, regex=True)

new_schedule_total_score = new_schedule_total_score.replace({'New York Mets':"N.Y. Mets"}, regex=True)
new_schedule_total_score = new_schedule_total_score.replace({'Philadelphia Phillies':"Philadelphia"}, regex=True)
new_schedule_total_score = new_schedule_total_score.replace({'Baltimore Orioles':"Baltimore"}, regex=True)
new_schedule_total_score = new_schedule_total_score.replace({'Seattle Mariners':"Seattle"}, regex=True)
new_schedule_total_score = new_schedule_total_score.replace({'Minnesota Twins':"Minnesota"}, regex=True)
new_schedule_total_score = new_schedule_total_score.replace({'Boston Red Sox':"Boston"}, regex=True)
new_schedule_total_score = new_schedule_total_score.replace({'Los Angeles Dodgers':"L.A. Dodgers"}, regex=True)
new_schedule_total_score = new_schedule_total_score.replace({'Colorado Rockies':"Colorado"}, regex=True)
new_schedule_total_score = new_schedule_total_score.replace({'\\"': ''}, regex=True)
new_schedule_total_score = new_schedule_total_score.replace({'\\]': ''}, regex=True)
new_schedule_total_score = new_schedule_total_score.replace({'\\[': ''}, regex=True)
new_schedule_total_score = new_schedule_total_score.replace({"\\'": ''}, regex=True)
new_schedule_total_score = new_schedule_total_score.drop_duplicates(subset=['HOME TEAM:', 'AWAY TEAM:'], keep='first')
new_schedule_total_score['HOME TEAM:'].replace('', np.nan, inplace=True)
new_schedule_total_score.dropna(subset=['HOME TEAM:'], inplace=True)
new_schedule_total_score['HOME TEAM POINTS:'].replace('', np.nan, inplace=True)
new_schedule_total_score.dropna(subset=['HOME TEAM POINTS:'], inplace=True)
df2 = new_schedule_total_score.apply(lambda x: pd.to_numeric(x.astype(str).str.replace(',', ''), errors='coerce'))
df3 = df2.fillna(new_schedule_total_score)
df3 = df3.sort_values(by=['HOME TEAM:'],ascending=True)
df3 = df3.drop_duplicates(subset=['HOME TEAM:', 'AWAY TEAM:'], keep='first')

stats_doc = ExcelWriter('pints.xlsx', engine='openpyxl')
df3.to_excel(stats_doc, sheet_name='Sheet1', index=False)
stats_doc.close()

print(df3)










yesterday = date.today() - timedelta(+1)


stats_doc3 = ExcelWriter(yesterday.strftime('Total_Points_PREV_DAY_%Y_%m_%d.xlsx'), engine='openpyxl')

new_schedule_total_score.to_excel(stats_doc3, sheet_name='Sheet1', index=False)

stats_doc3.close()