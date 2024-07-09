import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="yash 12345 yash @",database = "school2")
mycursor=mydb.cursor()
sql="delete from fee where FeeDeposit=220"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,"value deleted")
