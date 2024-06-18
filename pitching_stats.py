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

page = requests.get('https://www.cbssports.com/mlb/stats/team/team/pitching/mlb/regular/')

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
games_played = list()
innings_pitched = list()
.close()s_list = list()
.close()_opportunities = list()
total_hits = list()
total_runs = list()
home_runs = list()
errored_runs = list()
errored_runs_avg = list()
basae_on_balls = list()
strike_outs = list()
walk_and_hits_per_inning = list()






for teams in refs:
    yahoo += 1
    ##print(yahoo)
    team_all_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[1]/span/div/div[2]/div/span/a/text()', d1_page1_point_margin_list_var=yahoo))
    print(team_all_to_list)
    team_list.append(team_all_to_list)
    games_played_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[2]/text()', d1_page1_point_margin_list_var=yahoo))
    print(games_played_to_list)
    games_played.append(games_played_to_list)
    innings_pitched_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[3]/text()',d1_page1_point_margin_list_var=yahoo))
    print(innings_pitched_to_list)
    innings_pitched.append(innings_pitched_to_list)
    .close()s_list_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[6]/text()',d1_page1_point_margin_list_var=yahoo))
    print(.close()s_list_to_list)
    .close()s_list.append(.close()s_list_to_list)
    .close()_opportunities_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[7]/text()',d1_page1_point_margin_list_var=yahoo))
    print(.close()_opportunities_to_list)
    .close()_opportunities.append(.close()_opportunities_to_list)
    total_runs_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[8]/text()',d1_page1_point_margin_list_var=yahoo))
    print(total_runs_to_list)
    total_runs.append((total_runs_to_list))
    total_hits_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[9]/text()',d1_page1_point_margin_list_var=yahoo))
    print(total_hits_to_list)
    total_hits.append((total_hits_to_list))
    home_runs_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[10]/text()',d1_page1_point_margin_list_var=yahoo))
    print(home_runs_to_list)
    home_runs.append(home_runs_to_list)
    errored_runs_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[11]/text()',d1_page1_point_margin_list_var=yahoo))
    print(errored_runs_to_list)
    errored_runs.append(errored_runs_to_list)
    errored_runs_avg_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[12]/text()',d1_page1_point_margin_list_var=yahoo))
    print(errored_runs_avg_to_list)
    errored_runs_avg.append(errored_runs_avg_to_list)
    basae_on_balls_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[13]/text()',d1_page1_point_margin_list_var=yahoo))
    print(basae_on_balls_to_list)
    basae_on_balls.append(basae_on_balls_to_list)
    strike_outs_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[14]/text()',d1_page1_point_margin_list_var=yahoo))
    print(strike_outs_to_list)
    strike_outs.append(strike_outs_to_list)
    walk_and_hits_per_inning_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[15]/text()',d1_page1_point_margin_list_var=yahoo))
    print(walk_and_hits_per_inning_to_list)
    walk_and_hits_per_inning.append(walk_and_hits_per_inning_to_list)




dataframe_team_total_points_total_games = pd.DataFrame({'TEAM:': team_list, 'GAMES PLAYED:': games_played , 'INNINGS PITCHED:': innings_pitched, '.close()S PITCHING:': .close()s_list, '.close() OPPORTUNITY PITCHING:': .close()_opportunities, 'TOTAL HITS PITCHING:': total_hits, 'TOTAL RUNS PITCHING:': total_runs, 'HOME RUNS PITCHING:': home_runs, 'ERRORED RUNS PITCHING:': errored_runs, 'ERRORED RUNS AVG PITCHING:': errored_runs_avg, 'BASES ON BALLS PITCHING:': basae_on_balls, 'STRIKE OUTS PITCHING:': strike_outs, 'WALKS AND HITS PER INNING PITCHING:': walk_and_hits_per_inning})

print(dataframe_team_total_points_total_games)

stats_doc = ExcelWriter('MLB_PITCHING_STATS.xlsx')
dataframe_team_total_points_total_games.to_excel(stats_doc, sheet_name='Sheet1', index=False)
stats_doc.close()


excel_data_df2 = pd.read_excel('MLB_PITCHING_STATS.xlsx', sheet_name='Sheet1', engine='openpyxl')
excel_data_df2 = excel_data_df2.replace({'\\[':''}, regex=True)
excel_data_df2 = excel_data_df2.replace({'\\]':''}, regex=True)
excel_data_df2 = excel_data_df2.replace({"\\'":''}, regex=True)
excel_data_df2 = excel_data_df2.replace({"\"":''}, regex=True)
excel_data_df2 = excel_data_df2.replace({'\'':''}, regex=True)
excel_data_df2 = excel_data_df2.replace({"\\\\":''}, regex=True)
excel_data_df2 = excel_data_df2.replace({"n                    ":''}, regex=True)
excel_data_df2 = excel_data_df2.replace({"n                ":''}, regex=True)
excel_data_df2 = excel_data_df2.sort_values(by=['TEAM:'],ascending=True)
stats_doc = ExcelWriter('MLB_PITCHING_STATS.xlsx', engine='openpyxl')
excel_data_df2.to_excel(stats_doc, sheet_name='Sheet1', index=False)
stats_doc.close()