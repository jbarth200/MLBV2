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

page = requests.get('https://www.cbssports.com/mlb/stats/team/team/extended-batting/mlb/regular/')

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
total_bases = list()
sacrafice_hits = list()
sacrafice_files = list()
grounded_into_doubles = list()
triple_plate_apperances = list()
hit_by_pitch = list()
int_base_on_walks = list()
ground_balls = list()
fly_balls = list()
ground_to_fly_ratio = list()






for teams in refs:
    yahoo += 1
    ##print(yahoo)
    team_all_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[1]/span/div/div[2]/div/span/a/text()', d1_page1_point_margin_list_var=yahoo))
    print(team_all_to_list)
    team_list.append(team_all_to_list)
    total_bases_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[3]/text()', d1_page1_point_margin_list_var=yahoo))
    print(total_bases_to_list)
    total_bases.append(total_bases_to_list)
    sacrafice_hits_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[4]/text()',d1_page1_point_margin_list_var=yahoo))
    print(sacrafice_hits_to_list)
    sacrafice_hits.append(sacrafice_hits_to_list)
    sacrafice_files_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[5]/text()',d1_page1_point_margin_list_var=yahoo))
    print(sacrafice_files_to_list)
    sacrafice_files.append(sacrafice_files_to_list)
    grounded_into_doubles_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[6]/text()',d1_page1_point_margin_list_var=yahoo))
    print(grounded_into_doubles_to_list)
    grounded_into_doubles.append(grounded_into_doubles_to_list)
    total_doubles_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[8]/text()',d1_page1_point_margin_list_var=yahoo))
    print(total_doubles_to_list)
    hit_by_pitch.append((total_doubles_to_list))
    triple_plate_apperances_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[7]/text()',d1_page1_point_margin_list_var=yahoo))
    print(triple_plate_apperances_to_list)
    triple_plate_apperances.append((triple_plate_apperances_to_list))
    int_base_on_walks_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[9]/text()',d1_page1_point_margin_list_var=yahoo))
    print(int_base_on_walks_to_list)
    int_base_on_walks.append(int_base_on_walks_to_list)
    ground_balls_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[10]/text()',d1_page1_point_margin_list_var=yahoo))
    print(ground_balls_to_list)
    ground_balls.append(ground_balls_to_list)
    fly_balls_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[11]/text()',d1_page1_point_margin_list_var=yahoo))
    print(fly_balls_to_list)
    fly_balls.append(fly_balls_to_list)
    ground_to_fly_ratio_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[12]/text()',d1_page1_point_margin_list_var=yahoo))
    print(ground_to_fly_ratio_to_list)
    ground_to_fly_ratio.append(ground_to_fly_ratio_to_list)



dataframe_team_total_points_total_games = pd.DataFrame({'TEAM:': team_list, "TOTAL BASES BATTING": total_bases, 'SACRAFICE HITS BATTING:': sacrafice_hits, 'SACRAFICE FLIES BATTING:': sacrafice_files, 'GROUNDED INTO DOUBLES BATTING:': grounded_into_doubles, 'TRIPLE PLATE APPEARANCES BATTING:': triple_plate_apperances, 'HIT BY PITCH BATTING:': hit_by_pitch, 'INT BASE WALKED BATTING:': int_base_on_walks, 'GROUND_BALLS BATTING:': ground_balls, 'FLY BALLS BATTING:': fly_balls, 'GROUND TO FLY BATTING:': ground_to_fly_ratio})

print(dataframe_team_total_points_total_games)

stats_doc = ExcelWriter('MLB_EXTENDED_BATTING_STATS.xlsx')
dataframe_team_total_points_total_games.to_excel(stats_doc, sheet_name='Sheet1', index=False)
stats_doc.close()


excel_data_df2 = pd.read_excel('MLB_EXTENDED_BATTING_STATS.xlsx', sheet_name='Sheet1', engine='openpyxl')
excel_data_df2 = excel_data_df2.replace({'\\[':''}, regex=True)
excel_data_df2 = excel_data_df2.replace({'\\]':''}, regex=True)
excel_data_df2 = excel_data_df2.replace({"\\'":''}, regex=True)
excel_data_df2 = excel_data_df2.replace({"\"":''}, regex=True)
excel_data_df2 = excel_data_df2.replace({'\'':''}, regex=True)
excel_data_df2 = excel_data_df2.replace({"\\\\":''}, regex=True)
excel_data_df2 = excel_data_df2.replace({"n                    ":''}, regex=True)
excel_data_df2 = excel_data_df2.replace({"n                ":''}, regex=True)
excel_data_df2 = excel_data_df2.sort_values(by=['TEAM:'],ascending=True)
stats_doc = ExcelWriter('MLB_EXTENDED_BATTING_STATS.xlsx', engine='openpyxl')
excel_data_df2.to_excel(stats_doc, sheet_name='Sheet1', index=False)
stats_doc.close()