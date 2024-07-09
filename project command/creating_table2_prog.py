import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="school2")
mycursor=mydb.cursor()
mycursor.execute("create table fee(rollno int(5) references Student(roll), FeeDeposit int(6) NOT NULL, month varchar(10))")


