import mysql.connector as mysql
mydb=mysql.connect(host="localhost",user="root",passwd="yash 12345 yash @",database="yash")
mycursor=mydb.cursor()
sql="drop table employee"
mycursor.execute(sql)
mydb.commit()
print("table deleted")
