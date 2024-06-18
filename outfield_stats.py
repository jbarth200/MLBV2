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

page = requests.get('https://www.cbssports.com/mlb/stats/team/team/fielding/mlb/regular/')

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
total_catches = list()
total_errors = list()
total_put_outs = list()
total_assists = list()
passed_balls = list()
pick_off = list()
fielding_percent = list()
stolen_base_attempts = list()
caught_stealing = list()







for teams in refs:
    yahoo += 1
    ##print(yahoo)
    team_all_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[1]/span/div/div[2]/div/span/a/text()', d1_page1_point_margin_list_var=yahoo))
    print(team_all_to_list)
    team_list.append(team_all_to_list)
    total_catches_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[3]/text()', d1_page1_point_margin_list_var=yahoo))
    print(total_catches_to_list)
    total_catches.append(total_catches_to_list)
    total_errors_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[4]/text()',d1_page1_point_margin_list_var=yahoo))
    print(total_errors_to_list)
    total_errors.append(total_errors_to_list)
    total_put_outs_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[5]/text()',d1_page1_point_margin_list_var=yahoo))
    print(total_put_outs_to_list)
    total_put_outs.append(total_put_outs_to_list)
    total_assists_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[6]/text()',d1_page1_point_margin_list_var=yahoo))
    print(total_assists_to_list)
    total_assists.append(total_assists_to_list)
    pick_off_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[8]/text()',d1_page1_point_margin_list_var=yahoo))
    print(pick_off_to_list)
    pick_off.append((pick_off_to_list))
    passed_balls_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[7]/text()',d1_page1_point_margin_list_var=yahoo))
    print(passed_balls_to_list)
    passed_balls.append((passed_balls_to_list))
    fielding_percent_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[9]/text()',d1_page1_point_margin_list_var=yahoo))
    print(fielding_percent_to_list)
    fielding_percent.append(fielding_percent_to_list)
    stolen_base_attempts_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[10]/text()',d1_page1_point_margin_list_var=yahoo))
    print(stolen_base_attempts_to_list)
    stolen_base_attempts.append(stolen_base_attempts_to_list)
    caught_stealing_to_list = (tree.xpath('//*[@id="TableBase"]/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[11]/text()',d1_page1_point_margin_list_var=yahoo))
    print(caught_stealing_to_list)
    caught_stealing.append(caught_stealing_to_list)



dataframe_team_total_points_total_games = pd.DataFrame({'TEAM:': team_list, "TOTAL CATCHES:": total_catches, 'TOTAL ERRORS FIELDING:': total_errors, 'TOTAL PUT OUTS FIELDING:': total_put_outs, 'TOTAL ASSISTS FIELDING:': total_assists, 'PASSED BALLS FIELDING:': passed_balls, 'PICK OFF FIELDING:': pick_off, 'FIELDING PERCENT:': fielding_percent, 'STOLEN BASE ATTEMPTS FIELDING:': stolen_base_attempts, 'CAUGHT STEALING FIELDING:': caught_stealing})

print(dataframe_team_total_points_total_games)

stats_doc = ExcelWriter('MLB_FIELDING_STATS.xlsx')
dataframe_team_total_points_total_games.to_excel(stats_doc, sheet_name='Sheet1', index=False)
stats_doc.close()


excel_data_df2 = pd.read_excel('MLB_FIELDING_STATS.xlsx', sheet_name='Sheet1', engine='openpyxl')
excel_data_df2 = excel_data_df2.replace({'\\[':''}, regex=True)
excel_data_df2 = excel_data_df2.replace({'\\]':''}, regex=True)
excel_data_df2 = excel_data_df2.replace({"\\'":''}, regex=True)
excel_data_df2 = excel_data_df2.replace({"\"":''}, regex=True)
excel_data_df2 = excel_data_df2.replace({'\'':''}, regex=True)
excel_data_df2 = excel_data_df2.replace({"\\\\":''}, regex=True)
excel_data_df2 = excel_data_df2.replace({"n                    ":''}, regex=True)
excel_data_df2 = excel_data_df2.replace({"n                ":''}, regex=True)
excel_data_df2 = excel_data_df2.sort_values(by=['TEAM:'],ascending=True)
stats_doc = ExcelWriter('MLB_FIELDING_STATS.xlsx', engine='openpyxl')
excel_data_df2.to_excel(stats_doc, sheet_name='Sheet1', index=False)
stats_doc.close()