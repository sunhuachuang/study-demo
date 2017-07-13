import mysql.connector
# mysql-connector-python-rf

conn = mysql.connector.connect(user='root', password='sun', database='kg')
cursor = conn.cursor()

cursor.execute('create table users (name varchar(10), age int(3))')
cursor.commit()
cursor.close()
