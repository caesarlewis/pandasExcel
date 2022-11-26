import pandas as pd
import sqlalchemy
import pyodbc

connection = pyodbc.connect('DRIVER={SQL Server}; SERVER=(local); DATABASE=AdventureWorks;USER=sa;PASSWORD=123456')

query = 'SELECT FirstName, LastName FROM Person.Person'

df1 = pd.read_sql_query(query, connection)

print(df1.head())


query = "SELECT FirstName, LastName FROM Person.Person where FirstName = 'Timothy'"
engine = sqlalchemy.create_engine('mssql+pyodbc://sa:123456@(local)/AdventureWorks?driver=SQL+Server')
df2 = pd.read_sql_query(query, engine)

print(df2.head())