import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="school")
mycursor=mydb.cursor()
mycursor.execute("create table fee(rollno int(5),FeeDeposit int(6) , month varchar(10))")
