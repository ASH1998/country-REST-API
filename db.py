import csv
import sqlite3 as sql


conn = sql.connect('database.db')
cur = conn.cursor()
cur.execute('CREATE TABLE cocap_new (country, capital);')

with open('base.csv', 'r') as fin:
    dr = csv.DictReader(fin)
    to_db = [(i['Country'].lower(), i['Capital'].lower()) for i in dr]

cur.executemany("INSERT INTO cocap_new (country, capital) VALUES (?,?);", to_db)
conn.commit()
conn.close()