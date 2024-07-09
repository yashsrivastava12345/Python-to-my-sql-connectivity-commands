import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="yash 12345 yash @",database="school2")
mycursor = mydb.cursor()
sql="Select * From student "
#val=input("Enter name:")
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
