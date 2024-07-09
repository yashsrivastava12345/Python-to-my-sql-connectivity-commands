import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database = "carrer_objective")
mycursor=mydb.cursor()
sql="alter table carrerobjective add(stream char(30))"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,"Query affected")
