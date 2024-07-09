import mysql.connector as mysql
mydb = mysql.connect(host="localhost",user="root",passwd="")
mycursor=mydb.cursor()
mycursor.execute("create database school")
print ("database created") 

