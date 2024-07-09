import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="yash 12345 yash @",database = "school2")
mycursor=mydb.cursor()
sql="show databases"
mycursor.execute(sql)
for i in mycursor:
    print(i)
