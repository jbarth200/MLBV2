import pandas as pd
from pandas import ExcelWriter
from datetime import date, timedelta
yesterday = date.today() - timedelta(+1)


excel_data_df2 = pd.read_excel(yesterday.strftime('Total_Points_PREV_DAY_%Y_%m_%d.xlsx'), sheet_name='Sheet1', engine='openpyxl')
df2 = excel_data_df2.apply(lambda x: pd.to_numeric(x.astype(str).str.replace(',',''), errors='coerce'))
df3 = df2.fillna(excel_data_df2)
stats_doc = ExcelWriter(yesterday.strftime('Total_Points_PREV_DAY_%Y_%m_%d.xlsx'), engine='openpyxl')
df3.to_excel(stats_doc, sheet_name='Sheet1', index=False)
stats_doc.close()