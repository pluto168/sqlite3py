import sqlite3 
from sqlalchemy import create_engine, select, MetaData, Table, Table, Column, Integer,String
from sqlalchemy.orm import sessionmaker

conn = sqlite3.connect("datafile.db")
cursor = conn.cursor()

name = input("Please type the name you want to search: ")

result = cursor.execute(
    """select * from people where name = ?""", (name,)
)

#cursor.execute(
#    """CREATE TABLE people (id INTEGER PRIMARY KEY, name TEXT, count INTEGER)"""
#)


#cursor.execute("""INSERT INTO people (name, count) VALUES ('Bob', 15)""")


conn.commit()


cursor.close()
conn.close()
