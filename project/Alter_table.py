import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database = "school2")
mycursor=mydb.cursor()
sql="alter table student add(marks int(3))"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,"Query affected")
