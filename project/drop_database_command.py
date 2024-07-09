import mysql.connector as mysql
mydb=mysql.connect(host="localhost",user="root",passwd="yash 12345 yash @")
mycursor=mydb.cursor()
sql="drop database school3"
mycursor.execute(sql)
#mydb.commit()
print("database deleted")
