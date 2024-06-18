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

page = requests.get('https://www.cbssports.com/nhl/stats/team/team/scoring/nhl/regular/')

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
goals_total = list()
goals_per_game = list()
assists_total = list()
points_total = list()
points_per_game = list()
shots_on_goal_total = list()
shots_on_goal_per_game = list()
shots_on_goal_percentage = list()
power_play_goals = list()
power_play_goals_per_game = list()
short_handed_goals = list()







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
    goals_total.append(total_win_to_list)
    total_loss_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[4]/text()',d1_page1_point_margin_list_var=yahoo))
    print(total_loss_to_list)
    assists_total.append(total_loss_to_list)
    total_overtinme_loss_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[5]/text()',d1_page1_point_margin_list_var=yahoo))
    print(total_overtinme_loss_to_list)
    points_total.append(total_overtinme_loss_to_list)
    total_goals_against_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[6]/text()',d1_page1_point_margin_list_var=yahoo))
    print(total_goals_against_to_list)
    shots_on_goal_percentage.append((total_goals_against_to_list))
    total_goals_against_average_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[7]/text()',d1_page1_point_margin_list_var=yahoo))
    print(total_goals_against_average_to_list)
    shots_on_goal_total.append((total_goals_against_average_to_list))
    total_shots_against_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[8]/text()',d1_page1_point_margin_list_var=yahoo))
    print(total_shots_against_to_list)
    power_play_goals.append(total_shots_against_to_list)
    total_.close()s_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[9]/text()',d1_page1_point_margin_list_var=yahoo))
    print(total_.close()s_to_list)
    short_handed_goals.append(total_.close()s_to_list)





dataframe_team_total_points_total_games = pd.DataFrame({'TEAM:': team_list, 'GAMES PLAYED:': games_play, 'TOTAL GOALS:': goals_total, 'TOTAL ASSISTS:': assists_total, 'TOTAL POINTS:': points_total, 'TOTAL SHOTS ON GOAL:': shots_on_goal_percentage, 'SHOTS ON GOAL %:': shots_on_goal_total, 'TOTAL POWER PLAY GOALS:': power_play_goals, 'SHORT HANDED GOALS:': short_handed_goals})

print(dataframe_team_total_points_total_games)

stats_doc = ExcelWriter('NHL_SCORING_STATS.xlsx')
dataframe_team_total_points_total_games.to_excel(stats_doc, sheet_name='Sheet1', index=False)
stats_doc.close()


excel_data_df2 = pd.read_excel('NHL_SCORING_STATS.xlsx', sheet_name='Sheet1', engine='openpyxl')
excel_data_df2 = excel_data_df2.replace({'\\[':''}, regex=True)
excel_data_df2 = excel_data_df2.replace({'\\]':''}, regex=True)
excel_data_df2 = excel_data_df2.replace({"\\'":''}, regex=True)
excel_data_df2 = excel_data_df2.replace({"\"":''}, regex=True)
excel_data_df2 = excel_data_df2.replace({'\'':''}, regex=True)
excel_data_df2 = excel_data_df2.replace({"\\\\":''}, regex=True)
excel_data_df2 = excel_data_df2.replace({"n                    ":''}, regex=True)
excel_data_df2 = excel_data_df2.replace({"n                ":''}, regex=True)
excel_data_df2 = excel_data_df2.sort_values(by=['TEAM:'],ascending=True)
stats_doc = ExcelWriter('NHL_SCORING_STATS.xlsx', engine='openpyxl')
excel_data_df2.to_excel(stats_doc, sheet_name='Sheet1', index=False)
stats_doc.close()