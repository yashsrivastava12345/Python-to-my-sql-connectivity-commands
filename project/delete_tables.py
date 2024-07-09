import mysql.connector as mysql
mydb = mysql.connect(host="localhost",user="root",passwd="",database="carrer_objective")
mycursor=mydb.cursor()
mycursor.execute("drop table PCM")
mycursor.execute("drop table PCb")
mycursor.execute("drop table COMMERS")
print ("tables deleted") 
