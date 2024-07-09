import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database = "carrer_objective")
mycursor=mydb.cursor()
sql="delete from carrerobjective where nameofstudent='A'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,"value deleted")
