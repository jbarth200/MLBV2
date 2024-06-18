import pandas as pd
from pandas import ExcelWriter




excel_data_df = pd.read_excel('MLB_BATTING_STATS.xlsx', sheet_name='Sheet1', engine='openpyxl')
excel_data_df2 = pd.read_excel('MLB_EXTENDED_BATTING_STATS.xlsx', sheet_name='Sheet1', engine='openpyxl')
del excel_data_df2["TEAM:"]
excel_data_df3 = pd.read_excel('MLB_PITCHING_STATS.xlsx', sheet_name='Sheet1', engine='openpyxl')
del excel_data_df3["TEAM:"]
excel_data_df4 = pd.read_excel('MLB_EXTENDED_PITCHING_STATS.xlsx', sheet_name='Sheet1', engine='openpyxl')
del excel_data_df4["TEAM:"]
excel_data_df5 = pd.read_excel('MLB_FIELDING_STATS.xlsx', sheet_name='Sheet1', engine='openpyxl')
del excel_data_df5["TEAM:"]



finished_list = pd.concat([excel_data_df,excel_data_df2,excel_data_df3,excel_data_df4,excel_data_df5], axis=1)
stats_doc = ExcelWriter('MLB_STATS_ALL.xlsx', engine='openpyxl')
finished_list.to_excel(stats_doc, sheet_name='Sheet1', index=False)
stats_doc.close()
print(finished_list)


excel_data_df2 = pd.read_excel('MLB_STATS_ALL.xlsx', sheet_name='Sheet1', engine='openpyxl')
excel_data_df2 = excel_data_df2.replace({'â€”':'0'}, regex=True)
df2 = excel_data_df2.apply(lambda x: pd.to_numeric(x.astype(str).str.replace(',',''), errors='coerce'))
df3 = df2.fillna(excel_data_df2)
stats_doc = ExcelWriter('MLB_STATS.xlsx', engine='openpyxl')
df3.to_excel(stats_doc, sheet_name='Sheet1', index=False)
stats_doc.close()