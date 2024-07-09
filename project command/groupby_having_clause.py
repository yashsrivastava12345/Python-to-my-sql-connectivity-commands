import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="yash 12345 yash @",database = "school2")
mycursor=mydb.cursor()
sql="SELECT class, sum(marks) FROM student GROUP BY class HAVING sum(marks)>500;"
mycursor.execute(sql)
#mydb.commit()
#print(mycursor.rowcount,"Query affected")
for x in mycursor:
    print(x)

