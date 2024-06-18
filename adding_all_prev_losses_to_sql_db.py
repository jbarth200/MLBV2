import pandas as pd
from lxml import etree
from io import StringIO
from pandas import ExcelWriter
from datetime import date, timedelta
import datetime
import time

start_date = datetime.date(2021, 7, 30)
end_date = datetime.date(2021, 7, 30)
delta = datetime.timedelta(days=1)

import sqlalchemy

database_username = 'root'
database_password = ''
database_ip = 'localhost'
database_name = 'personal'
database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                               format(database_username, database_password,
                                                    database_ip, database_name))

while start_date <= end_date:
    print(start_date)
    start_date += delta
    excel_data_df2 = pd.read_excel(time.strftime('Total_Points2_%Y_%m_%d.xlsx'), engine='openpyxl')
    excel_data_df2 = excel_data_df2.replace({'\\[':''}, regex=True)
    excel_data_df2 = excel_data_df2.replace({'\\]':''}, regex=True)
    excel_data_df2.to_sql(con=database_connection, name='mlb_v5', if_exists='append', index=False)