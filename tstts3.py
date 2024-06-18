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

# Set explicit HTMLParser
parser = etree.HTMLParser()

page = requests.get('https://www.cbssports.com/nhl/stats/team/team/penalties/nhl/regular/')

# Decode the page content from bytes to string
html = page.content.decode("cp1252")

# Create your etree with a StringIO object which functions similarly
# to a fileHandler
tree = etree.parse(StringIO(html), parser=parser)
## Creating var for page path MAYBE?!?!?!
refs = tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr')
print(len(refs))


##Creating our start for iteration
yahoo = 0

##Creating our blank lists
team_list = list()
games_play = list()
total_penalty_mins = list()
total_major_penalty_mins = list()
total_min_penalty_mins = list()








for teams in refs:
    yahoo += 1
    ##print(yahoo)
    team_all_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[1]/span/div/div[2]/div/span/a/text()', d1_page1_point_margin_list_var=yahoo))
    print(team_all_to_list)
    team_list.append(team_all_to_list)
    games_played_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[2]/text()', d1_page1_point_margin_list_var=yahoo))
    print(team_all_to_list)
    games_play.append(games_played_to_list)
    total_win_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[3]/text()',d1_page1_point_margin_list_var=yahoo))
    print(total_win_to_list)
    total_penalty_mins.append(total_win_to_list)
    total_loss_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[4]/text()',d1_page1_point_margin_list_var=yahoo))
    print(total_loss_to_list)
    total_major_penalty_mins.append(total_loss_to_list)
    total_loss_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[5]/text()',d1_page1_point_margin_list_var=yahoo))
    print(total_loss_to_list)
    total_min_penalty_mins.append(total_loss_to_list)




dataframe_team_total_points_total_games = pd.DataFrame({'TEAM:': team_list, 'GAMES PLAYED:': games_play, 'TOTAL PENALTY MINS:': total_penalty_mins, 'TOTAL MAJOR PENALTY MINS:': total_major_penalty_mins, 'TOTAL MIN PENALTY MINS:': total_min_penalty_mins})

print(dataframe_team_total_points_total_games)

stats_doc = ExcelWriter('NHL_PENALTY_STATS.xlsx')
dataframe_team_total_points_total_games.to_excel(stats_doc, sheet_name='Sheet1', index=False)
stats_doc.close()


excel_data_df2 = pd.read_excel('NHL_PENALTY_STATS.xlsx', sheet_name='Sheet1', engine='openpyxl')
excel_data_df2 = excel_data_df2.replace({'\\[':''}, regex=True)
excel_data_df2 = excel_data_df2.replace({'\\]':''}, regex=True)
excel_data_df2 = excel_data_df2.replace({"\\'":''}, regex=True)
excel_data_df2 = excel_data_df2.replace({"\"":''}, regex=True)
excel_data_df2 = excel_data_df2.replace({'\'':''}, regex=True)
excel_data_df2 = excel_data_df2.replace({"\\\\":''}, regex=True)
excel_data_df2 = excel_data_df2.replace({"n                    ":''}, regex=True)
excel_data_df2 = excel_data_df2.replace({"n                ":''}, regex=True)
excel_data_df2 = excel_data_df2.sort_values(by=['TEAM:'],ascending=True)
stats_doc = ExcelWriter('NHL_PENALTY_STATS.xlsx', engine='openpyxl')
excel_data_df2.to_excel(stats_doc, sheet_name='Sheet1', index=False)
stats_doc.close()