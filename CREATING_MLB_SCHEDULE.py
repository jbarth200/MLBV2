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

#################################################################################

# Set explicit HTMLParser
parser = etree.HTMLParser()

page = requests.get(time.strftime(('https://www.foxsports.com/mlb/scores')))

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


for teams in refs:
    yahoo += 1
    print(yahoo)
    away_team = tree.xpath('/html/body/form/div[2]/div[2]/div/div/main/div[2]/div[2]/div[2]/div[$d1_page1_point_margin_list_var]/table[1]/thead/tr/th[1]/a/span[1]/text()',d1_page1_point_margin_list_var=yahoo)
    home_team = tree.xpath('/html/body/form/div[2]/div[2]/div/div/main/div[2]/div[2]/div[2]/div[$d1_page1_point_margin_list_var]/table[1]/thead/tr/th[1]/a/span[2]/text()',d1_page1_point_margin_list_var=yahoo)
    game_status = tree.xpath('/html/body/form/div[2]/div[2]/div/div/main/div[2]/div[2]/div[2]/div[$d1_page1_point_margin_list_var]/table[1]/tbody/tr[1]/td/div/div[2]/div[2]/span/text()',d1_page1_point_margin_list_var=yahoo)
   ## print(team_all)
   ## team_list.append(team_all)
   ## print(refs2)
   ## turn_over_per_game.append(refs2)
    away_team_list.append(away_team)
    home_team_list.append(home_team)
    game_status_list.append(game_status)



print(away_team_list)
print(home_team_list)
print(game_status_list)


away_team_list.reverse()
home_team_list.reverse()
game_status_list.reverse()

dataframe_schedule = pd.DataFrame({'HOME TEAM:':home_team_list,'AWAY TEAM:':away_team_list, 'GAME STATUS:': game_status_list})
print(dataframe_schedule)

stats_doc = ExcelWriter('MLB_Schedule.xlsx')
dataframe_schedule.to_excel(stats_doc, sheet_name='Sheet1', index=False)
stats_doc.close()


excel_data_df2 = pd.read_excel('MLB_Schedule.xlsx', sheet_name='Sheet1', engine='openpyxl')
df2 = excel_data_df2.apply(lambda x: pd.to_numeric(x.astype(str).str.replace(',',''), errors='coerce'))
df3 = df2.fillna(excel_data_df2)
stats_doc = ExcelWriter('MLB_Schedule.xlsx', engine='openpyxl')
df3.to_excel(stats_doc, sheet_name='Sheet1', index=False)
stats_doc.close()




excel_data_df2 = pd.read_excel('MLB_Schedule.xlsx', sheet_name='Sheet1', engine='openpyxl')
excel_data_df2 = excel_data_df2.replace({'Miami Marlins':'Miami'}, regex=True)
excel_data_df2 = excel_data_df2.replace({'Atlanta Braves':'Atlanta'}, regex=True)
excel_data_df2 = excel_data_df2.replace({'Washington Nationals':'Washington'}, regex=True)
excel_data_df2 = excel_data_df2.replace({'St. Louis Cardinals':'St. Louis'}, regex=True)
excel_data_df2 = excel_data_df2.replace({'Cleveland Guardians':'Cleveland'}, regex=True)
excel_data_df2 = excel_data_df2.replace({'Chicago White Sox':'Chi. White Sox'}, regex=True)
excel_data_df2 = excel_data_df2.replace({'Los Angeles Angels':'L.A. Angels'}, regex=True)
excel_data_df2 = excel_data_df2.replace({'Kansas City Royals':'Kansas City'}, regex=True)
excel_data_df2 = excel_data_df2.replace({'Detroit Tigers':'Detroit'}, regex=True)
excel_data_df2 = excel_data_df2.replace({'Houston Astros':'Houston'}, regex=True)
excel_data_df2 = excel_data_df2.replace({'Oakland Athletics':'Oakland'}, regex=True)
excel_data_df2 = excel_data_df2.replace({'Arizona Diamondbacks':"Arizona"}, regex=True)
excel_data_df2 = excel_data_df2.replace({'Cincinnati Reds':"Cincinnati"}, regex=True)
excel_data_df2 = excel_data_df2.replace({'San Francisco Giants':"San Francisco"}, regex=True)
excel_data_df2 = excel_data_df2.replace({'San Diego Padres':"San Diego"}, regex=True)
excel_data_df2 = excel_data_df2.replace({'Pittsburgh Pirates':"Pittsburgh"}, regex=True)
excel_data_df2 = excel_data_df2.replace({'New York Yankees':"N.Y. Yankees"}, regex=True)

excel_data_df2 = excel_data_df2.replace({'Minnesota Wild':"Minnesota"}, regex=True)
excel_data_df2 = excel_data_df2.replace({'Toronto Blue Jays':"Toronto"}, regex=True)
excel_data_df2 = excel_data_df2.replace({'Texas Rangers':"Texas"}, regex=True)
excel_data_df2 = excel_data_df2.replace({'Tampa Bay Rays':"Tampa Bay"}, regex=True)
excel_data_df2 = excel_data_df2.replace({'Chicago Cubs':"Chi. Cubs"}, regex=True)
excel_data_df2 = excel_data_df2.replace({'Milwaukee Brewers':"Milwaukee"}, regex=True)

excel_data_df2 = excel_data_df2.replace({'New York Mets':"N.Y. Mets"}, regex=True)
excel_data_df2 = excel_data_df2.replace({'Philadelphia Phillies':"Philadelphia"}, regex=True)
excel_data_df2 = excel_data_df2.replace({'Baltimore Orioles':"Baltimore"}, regex=True)
excel_data_df2 = excel_data_df2.replace({'Seattle Mariners':"Seattle"}, regex=True)
excel_data_df2 = excel_data_df2.replace({'Minnesota Twins':"Minnesota"}, regex=True)
excel_data_df2 = excel_data_df2.replace({'Boston Red Sox':"Boston"}, regex=True)
excel_data_df2 = excel_data_df2.replace({'Los Angeles Dodgers':"L.A. Dodgers"}, regex=True)
excel_data_df2 = excel_data_df2.replace({'Colorado Rockies':"Colorado"}, regex=True)
excel_data_df2 = excel_data_df2.replace({'\\"':''}, regex=True)
excel_data_df2 = excel_data_df2.replace({'\\]':''}, regex=True)
excel_data_df2 = excel_data_df2.replace({'\\[':''}, regex=True)
excel_data_df2 = excel_data_df2.replace({"\\'":''}, regex=True)
excel_data_df2 = excel_data_df2[excel_data_df2['HOME TEAM:'] != ""]
excel_data_df2 = excel_data_df2[excel_data_df2['GAME STATUS:'] != "Postponed"]
excel_data_df2 = excel_data_df2.drop_duplicates(subset=['HOME TEAM:', 'AWAY TEAM:'], keep='first')
excel_data_df2 = excel_data_df2.drop_duplicates(subset='HOME TEAM:', keep="first")
stats_doc = ExcelWriter('MLB_Schedule.xlsx', engine='openpyxl')
excel_data_df2.to_excel(stats_doc, sheet_name='Sheet1', index=False)
stats_doc.close()




excel_data_df2 = pd.read_excel('MLB_Schedule.xlsx', sheet_name='Sheet1', engine='openpyxl')
df2 = excel_data_df2.apply(lambda x: pd.to_numeric(x.astype(str).str.replace(',',''), errors='coerce'))
df3 = df2.fillna(excel_data_df2)
stats_doc = ExcelWriter('MLB_Schedule.xlsx', engine='openpyxl')
df3.to_excel(stats_doc, sheet_name='Sheet1', index=False)
stats_doc.close()










