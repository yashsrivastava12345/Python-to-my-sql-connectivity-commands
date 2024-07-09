import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="yash 12345 yash @",database = "school2")
mycursor=mydb.cursor()
sql="update student set marks=399 where rollno=5"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,"vaues updated")
