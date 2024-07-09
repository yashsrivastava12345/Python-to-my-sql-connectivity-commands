import mysql.connector as mysql
mydb = mysql.connect(host="localhost",user="root",passwd="")
mycursor=mydb.cursor()
mycursor.execute("create database school2")
print ("database created") 

