import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="school2")
mycursor=mydb.cursor()
mycursor.execute("create table student(rollno int(4) not null primary key,name char(20) not null , age int(2) not null,class char(25)not null,city char(20))")


