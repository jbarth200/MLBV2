import pandas as pd
from pandas import ExcelWriter
import time
import numpy as np
import sqlalchemy
from datetime import date, timedelta
import sqlalchemy
yesterday = date.today() - timedelta(1)
database_username = 'root'
database_password = ''
database_ip = 'localhost'
database_name = 'mlb_24'
database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                               format(database_username, database_password,
                                                    database_ip, database_name))


excel_data_df4 = pd.read_excel(time.strftime('Total_Points2_%Y_%m_%d.xlsx'), sheet_name='Sheet1', engine='openpyxl')
excel_data_df4.to_sql(con=database_connection, name='mlb_v5', if_exists='replace', index=False)

