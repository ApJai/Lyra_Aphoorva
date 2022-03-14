import sys
import requests
import sqlite3
import pandas as pd


inFile = sys.argv[1]

data = pd.read_csv (inFile)   
df = pd.DataFrame(data)
print(df)


url = 'https://httpbin.org/post'
myobj = {'users': df}
x = requests.post(url, data = myobj)
#print the response text (the content of the requested file):
print(x.text)


conn = sqlite3.connect('user.db')
cursor = conn.cursor()

#create table users
cursor.execute('''
		CREATE TABLE users (
			FN nvarchar(50),
			LN nvarchar(50),
			ag2 int
			)
    ''')

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute('''INSERT INTO users(FN,LN,ag2) values(?,?,?);''', (row.FN, row.LN, row.ag2))

conn.commit()
conn.close()



