import mysql.connector as mysql
mydb=mysql.connect(host="localhost",user="root",passwd="yash 12345 yash @")
mycursor=mydb.cursor()
sql="create database school4"
mycursor.execute(sql)
mydb.commit()
print("database created")
