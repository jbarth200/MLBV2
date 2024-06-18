import pandas as pd
from lxml import etree
from io import StringIO
from pandas import ExcelWriter
from datetime import date, timedelta
import datetime

start_date = datetime.date(2021, 5, 12)
end_date = datetime.date(2021, 6, 6)
delta = datetime.timedelta(days=1)

while start_date <= end_date:
    print(start_date)
    start_date += delta
    excel_data_df2 = pd.read_excel(start_date.strftime('Total_Points_PREV_DAY_%Y_%m_%d.xlsx'), sheet_name='Sheet1', engine='openpyxl')
    #excel_data_df2 = excel_data_df2.replace({'\\"':''}, regex=True)
    excel_data_df2 = excel_data_df2.replace({'\\[':''}, regex=True)
    excel_data_df2 = excel_data_df2.replace({'\\]':''}, regex=True)
    #excel_data_df2 = excel_data_df2.replace({"\\'":''}, regex=True)
    stats_doc = ExcelWriter(start_date.strftime('Total_Points_PREV_DAY_%Y_%m_%d.xlsx'), engine='openpyxl')
    excel_data_df2.to_excel(stats_doc, sheet_name='Sheet1', index=False)
    stats_doc.close()


