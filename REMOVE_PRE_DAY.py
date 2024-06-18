import pandas as pd
from pandas import ExcelWriter
from datetime import date, timedelta
from pandas import ExcelWriter
yesterday = date.today() - timedelta(+1)

excel_data_df2 = pd.read_excel(yesterday.strftime('Total_Points_PREV_DAY_%Y_%m_%d.xlsx'), sheet_name='Sheet1', engine='openpyxl')
excel_data_df2 = excel_data_df2.replace({'\\[':''}, regex=True)
excel_data_df2 = excel_data_df2.replace({'\\]':''}, regex=True)
excel_data_df2 = excel_data_df2.replace({"\\'":''}, regex=True)
stats_doc = ExcelWriter(yesterday.strftime('Total_Points_PREV_DAY_%Y_%m_%d.xlsx'), engine='openpyxl')
excel_data_df2.to_excel(stats_doc, sheet_name='Sheet1', index=False)
stats_doc.close()