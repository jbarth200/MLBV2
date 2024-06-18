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

page = requests.get('https://www.cbssports.com/mlb/stats/team/team/batting/mlb/regular/')

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
total_average_hits = list()
total_at_bats = list()
total_runs = list()
total_hits = list()
total_doubles = list()
total_triples = list()
total_rbi = list()
total_homerun_batting = list()
total_base_walked_batting = list()
total_strike_out_batting = list()
total_on_base_percentage = list()
total_slugging_percentage = list()
total_on_base_plus_slugging = []





for teams in refs:
    yahoo += 1
    ##print(yahoo)
    team_all_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[1]/span/div/div[2]/div/span/a/text()', d1_page1_point_margin_list_var=yahoo))
    print(team_all_to_list)
    team_list.append(team_all_to_list)
    games_played_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[2]/text()', d1_page1_point_margin_list_var=yahoo))
    print(games_played_to_list)
    games_played.append(games_played_to_list)
    total_average_hits_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[3]/text()',d1_page1_point_margin_list_var=yahoo))
    print(total_average_hits_to_list)
    total_average_hits.append(total_average_hits_to_list)
    total_at_bats_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[4]/text()',d1_page1_point_margin_list_var=yahoo))
    print(total_at_bats_to_list)
    total_at_bats.append(total_at_bats_to_list)
    total_runs_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[5]/text()',d1_page1_point_margin_list_var=yahoo))
    print(total_runs_to_list)
    total_runs.append(total_runs_to_list)
    total_doubles_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[7]/text()',d1_page1_point_margin_list_var=yahoo))
    print(total_doubles_to_list)
    total_doubles.append((total_doubles_to_list))
    total_hits_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[6]/text()',d1_page1_point_margin_list_var=yahoo))
    print(total_hits_to_list)
    total_hits.append((total_hits_to_list))
    total_triples_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[8]/text()',d1_page1_point_margin_list_var=yahoo))
    print(total_triples_to_list)
    total_triples.append(total_triples_to_list)
    total_rbi_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[10]/text()',d1_page1_point_margin_list_var=yahoo))
    print(total_rbi_to_list)
    total_rbi.append(total_rbi_to_list)
    total_homerun_batting_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[9]/text()',d1_page1_point_margin_list_var=yahoo))
    print(total_homerun_batting_to_list)
    total_homerun_batting.append(total_homerun_batting_to_list)
    total_base_walked_batting_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[13]/text()',d1_page1_point_margin_list_var=yahoo))
    print(total_base_walked_batting_to_list)
    total_base_walked_batting.append(total_base_walked_batting_to_list)
    total_strike_out_batting_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[14]/text()',d1_page1_point_margin_list_var=yahoo))
    print(total_strike_out_batting_to_list)
    total_strike_out_batting.append(total_strike_out_batting_to_list)
    total_on_base_percentage_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[15]/text()',d1_page1_point_margin_list_var=yahoo))
    print(total_on_base_percentage_to_list)
    total_on_base_percentage.append(total_on_base_percentage_to_list)
    total_slugging_percentage_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[16]/text()',d1_page1_point_margin_list_var=yahoo))
    print(total_slugging_percentage_to_list)
    total_slugging_percentage.append(total_slugging_percentage_to_list)
    total_on_base_plus_slugging_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[17]/text()',d1_page1_point_margin_list_var=yahoo))
    print(total_on_base_plus_slugging_to_list)
    total_on_base_plus_slugging.append(total_on_base_plus_slugging_to_list)



dataframe_team_total_points_total_games = pd.DataFrame({'TEAM:': team_list, 'GAMES PLAYED:': games_played , 'TOTAL AVERAGE HITS BATTING:': total_average_hits, 'TOTAL AT BATS:': total_at_bats, 'TOTAL RUNS BATTING:': total_runs,'TOTAL HITS BATTING:': total_hits, 'TOTAL DOUBLES BATTING:': total_doubles, 'TOTAL TRIPLES BATTING:': total_triples, 'TOTAL RBI BATTING:': total_rbi, 'TOTAL HOME RUN BATTING:': total_homerun_batting, 'TOTAL BASES WALKED BATTING:': total_base_walked_batting, 'TOTAL STRIKE OUT BATTING:': total_strike_out_batting, 'TOTAL ON BASE PERCENTAGE BATTING:': total_on_base_percentage, 'TOTAL SLUGGING PERCENTAGE BATTING:': total_slugging_percentage, "TOTAL BASE ON PLUS SLUGGING PERCENTAGE BATTING:": total_on_base_plus_slugging})

print(dataframe_team_total_points_total_games)

stats_doc = ExcelWriter('MLB_BATTING_STATS.xlsx')
dataframe_team_total_points_total_games.to_excel(stats_doc, sheet_name='Sheet1', index=False)
stats_doc.close()


excel_data_df2 = pd.read_excel('MLB_BATTING_STATS.xlsx', sheet_name='Sheet1', engine='openpyxl')
excel_data_df2 = excel_data_df2.replace({'\\[':''}, regex=True)
excel_data_df2 = excel_data_df2.replace({'\\]':''}, regex=True)
excel_data_df2 = excel_data_df2.replace({"\\'":''}, regex=True)
excel_data_df2 = excel_data_df2.replace({"\"":''}, regex=True)
excel_data_df2 = excel_data_df2.replace({'\'':''}, regex=True)
excel_data_df2 = excel_data_df2.replace({"\\\\":''}, regex=True)
excel_data_df2 = excel_data_df2.replace({"n                    ":''}, regex=True)
excel_data_df2 = excel_data_df2.replace({"n                ":''}, regex=True)
excel_data_df2 = excel_data_df2.sort_values(by=['TEAM:'],ascending=True)
stats_doc = ExcelWriter('MLB_BATTING_STATS.xlsx', engine='openpyxl')
excel_data_df2.to_excel(stats_doc, sheet_name='Sheet1', index=False)
stats_doc.close()