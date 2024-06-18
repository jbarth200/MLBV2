import pandas as pd
from pandas import ExcelWriter


import time

from datetime import date, timedelta
import os
yesterday = date.today() - timedelta(1)

from shutil import copyfile
import time
from datetime import date, timedelta

##copyfile(yesterday.strftime('Total_Points_PREV_DAY_%Y_%m_%d.xlsx'), (yesterday.strftime('Total2_Points_PREV_DAY_%Y_%m_%d.xlsx')))

excel_data_df = pd.read_excel(yesterday.strftime(r'C:\Users\joshb\PycharmProjects\MLB_V6\Total_Points_PREV_DAY_%Y_%m_%d_orig.xlsx'), sheet_name='Sheet1', engine='openpyxl')
excel_data_df = excel_data_df.sort_values('HOME TEAM:')
print(excel_data_df)

print("EXCEL DATA DF ABBBBBBBBBBBBOVE")
##del excel_data_df['HOME TEAM:']
##del excel_data_df['AWAY TEAM:']
print(excel_data_df)
print("EXCEL DATA DF ABBBBBBBBBBBBOVE")
excel_data_df3 = pd.read_excel(yesterday.strftime('Total_Points2_%Y_%m_%d.xlsx'), sheet_name='Sheet1', engine='openpyxl')
excel_data_df3 = excel_data_df3.sort_values('HOME TEAM:')
print(excel_data_df3)
print("EXCEL DATA DF2 ABBBBBBBBBBBBOVE")



print("WHEREEEEEE AREAAAAAAAEFSDFJSDAKFJSDAKFJSALgfjasLRIgfjhASRLIKG")
##excel_data_df = excel_data_df.sort_index(axis=1 ,ascending=True)
excel_data_df = excel_data_df.iloc[::-1]
excel_data_df3 = excel_data_df3.iloc[::-1]

print(excel_data_df)
print(excel_data_df3)
new_schedule_score = excel_data_df3.merge(excel_data_df, on=['HOME TEAM:', 'AWAY TEAM:'])
stats_doc = ExcelWriter(yesterday.strftime('Total_Points_PREV_DAY_%Y_%m_%d.xlsx'), engine='openpyxl')
new_schedule_score.to_excel(stats_doc, sheet_name='Sheet1', index=False)
stats_doc.close()


print("ABOVE")
