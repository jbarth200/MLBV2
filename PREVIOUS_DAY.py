
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
import os

try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

#################################################################################
from datetime import date, timedelta



yesterday = date.today() - timedelta(+1)
from shutil import copyfile

##copyfile(yesterday.strftime('Total_Points2_%Y_%m_%d.xlsx'), (time.strftime('yesterdayscores_%Y_%m_%d.xlsx')))

# Set explicit HTMLParser
parser = etree.HTMLParser()

page = requests.get(yesterday.strftime('https://www.cbssports.com/nhl/schedule/%Y%m%d'))

# Decode the page content from bytes to string
html = page.content.decode("utf-8")

# Create your etree with a StringIO object which functions similarly
# to a fileHandler
tree = etree.parse(StringIO(html), parser=parser)
## Creating var for page path MAYBE?!?!?!
refs = tree.xpath("//*[@id='TableBase']/div/div/table/tbody/tr/text()")
print(refs)
number_of_games = len(refs) * .40 / 2
ttttt = int(number_of_games)
print(number_of_games)

## Creating length of teams listed
testssss = tree.xpath("//*[@id='TableBase']/div/div/table/tbody/tr[1]/td[1]/span/div/div[2]/div/span/a/text()")
testssss2 = tree.xpath("//*[@id='TableBase']/div/div/table/tbody/tr[1]/td[2]/span/div/div[2]/div/span/a/text()")
##print(testssss)
##print(testssss2)


##Creating our start for iteration
yahoo = 0

##Creating our blank lists
home_team_list = list()
away_team_list = list()
score = list()


for teams in range(ttttt):
    yahoo += 1
    ##print(yahoo)
    home_team = tree.xpath("//*[@id='TableBase']/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[1]/span/div/div[2]/div/span/a/text()", d1_page1_point_margin_list_var=yahoo)
    print(home_team)
    home_team_list.append(home_team)
    away_team = tree.xpath("//*[@id='TableBase']/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[2]/span/div/div[2]/div/span/a/text()", d1_page1_point_margin_list_var=yahoo)
    away_team_list.append(away_team)
    print(away_team)
    print(1)
    scores = tree.xpath("//*[@id='TableBase']/div/div/table/tbody/tr[$d1_page1_point_margin_list_var]/td[3]/div/a/text()", d1_page1_point_margin_list_var=yahoo)
    print(scores)
    score.append(scores)



print(home_team_list)
print(away_team_list)
print(score)


dataframe_nba_stats_all = pd.DataFrame({'AWAY TEAM:': home_team_list, 'HOME TEAM:': away_team_list})

print(dataframe_nba_stats_all)

stats_doc = ExcelWriter('PREVIOUS NHL GAME SCHEDULE.xlsx')
dataframe_nba_stats_all.to_excel(stats_doc, sheet_name='Sheet1', index=False)
stats_doc.close()
