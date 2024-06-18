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

page = requests.get('https://www.cbssports.com/mlb/stats/team/team/extended-pitching/mlb/regular/')

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
hold_list = list()
shutout_list = list()
quality_start = list()
balks_list = list()
wild_pitch = list()
total_pitches = list()
doubles = list()
triples = list()
homeruns = list()
hit_by_pitch = list()
int_base_on_ball = list()
on_base_percent = list()






for teams in refs:
    yahoo += 1
    ##print(yahoo)
    team_all_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[1]/span/div/div[2]/div/span/a/text()', d1_page1_point_margin_list_var=yahoo))
    print(team_all_to_list)
    team_list.append(team_all_to_list)
    hold_list_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[4]/text()', d1_page1_point_margin_list_var=yahoo))
    print(hold_list_to_list)
    hold_list.append(hold_list_to_list)
    shutout_list_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[6]/text()',d1_page1_point_margin_list_var=yahoo))
    print(shutout_list_to_list)
    shutout_list.append(shutout_list_to_list)
    quality_start_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[7]/text()',d1_page1_point_margin_list_var=yahoo))
    print(quality_start_to_list)
    quality_start.append(quality_start_to_list)
    balks_list_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[8]/text()',d1_page1_point_margin_list_var=yahoo))
    print(balks_list_to_list)
    balks_list.append(balks_list_to_list)
    total_pitches_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[10]/text()',d1_page1_point_margin_list_var=yahoo))
    print(total_pitches_to_list)
    total_pitches.append((total_pitches_to_list))
    wild_pitch_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[9]/text()',d1_page1_point_margin_list_var=yahoo))
    print(wild_pitch_to_list)
    wild_pitch.append((wild_pitch_to_list))
    doubles_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[11]/text()',d1_page1_point_margin_list_var=yahoo))
    print(doubles_to_list)
    doubles.append(doubles_to_list)
    triples_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[12]/text()',d1_page1_point_margin_list_var=yahoo))
    print(triples_to_list)
    triples.append(triples_to_list)
    homeruns_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[13]/text()',d1_page1_point_margin_list_var=yahoo))
    print(homeruns_to_list)
    homeruns.append(homeruns_to_list)
    hit_by_pitch_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[14]/text()',d1_page1_point_margin_list_var=yahoo))
    print(hit_by_pitch_to_list)
    hit_by_pitch.append(hit_by_pitch_to_list)
    int_base_on_ball_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[15]/text()',d1_page1_point_margin_list_var=yahoo))
    print(int_base_on_ball_to_list)
    int_base_on_ball.append(int_base_on_ball_to_list)
    on_base_percent_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[16]/text()',d1_page1_point_margin_list_var=yahoo))
    print(on_base_percent_to_list)
    on_base_percent.append(on_base_percent_to_list)




dataframe_team_total_points_total_games = pd.DataFrame({'TEAM:': team_list, 'HOLDS PITCHING:': hold_list , 'SHUTOUTS PITCHED:': shutout_list, 'QUALITY STARTS PITCHING:': quality_start, 'BALKS PITCHING:': balks_list, 'WILDS PITCHING:': wild_pitch, 'TOTAL PITCHES PITCHING:': total_pitches, 'DOUBLES PITCHING:': doubles, 'TRIPLES PITCHING:': triples, 'HOMERUNS PITCHING:': homeruns, 'HIT BY PITCH PITCHING:': hit_by_pitch, 'INT BASES ON BALLS PITCHING:': int_base_on_ball, 'ON BASE % PITCHING:': on_base_percent})

print(dataframe_team_total_points_total_games)

stats_doc = ExcelWriter('MLB_EXTENDED_PITCHING_STATS.xlsx')
dataframe_team_total_points_total_games.to_excel(stats_doc, sheet_name='Sheet1', index=False)
stats_doc.close()


excel_data_df2 = pd.read_excel('MLB_EXTENDED_PITCHING_STATS.xlsx', sheet_name='Sheet1', engine='openpyxl')
excel_data_df2 = excel_data_df2.replace({'\\[':''}, regex=True)
excel_data_df2 = excel_data_df2.replace({'\\]':''}, regex=True)
excel_data_df2 = excel_data_df2.replace({"\\'":''}, regex=True)
excel_data_df2 = excel_data_df2.replace({"\"":''}, regex=True)
excel_data_df2 = excel_data_df2.replace({'\'':''}, regex=True)
excel_data_df2 = excel_data_df2.replace({"\\\\":''}, regex=True)
excel_data_df2 = excel_data_df2.replace({"n                    ":''}, regex=True)
excel_data_df2 = excel_data_df2.replace({"n                ":''}, regex=True)
excel_data_df2 = excel_data_df2.sort_values(by=['TEAM:'],ascending=True)
stats_doc = ExcelWriter('MLB_EXTENDED_PITCHING_STATS.xlsx', engine='openpyxl')
excel_data_df2.to_excel(stats_doc, sheet_name='Sheet1', index=False)
stats_doc.close()