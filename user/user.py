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
			first_name nvarchar(50),
			second_name nvarchar(50),
			Age int
			)
    ''')

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute('''INSERT INTO users(first_name,second_name,Age) values(?,?,?);''', (row.first_name, row.second_name, row.Age))

conn.commit()
conn.close()



