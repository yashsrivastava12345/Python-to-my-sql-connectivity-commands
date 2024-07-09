import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="yash 12345 yash @",database="school2")
mycursor=mydb.cursor()
i=0
while True:
    cho=input("Enter your choice\n q to quit \n n for resuming to enter data\n: ")
    if cho=="Q" or cho=="q":
        break
    elif cho=="N" or cho=="n":
        a=int(input("Enter roll number: "))
        c=int(input("Enter feedeposit:"))
        d=input ("Enter month: ")
        sql="insert into fee (rollno,FeeDeposit,month) values (%s,%s,%s)"
        val=(a,c,d)
        mycursor.execute(sql,val)
        mydb.commit()
        print(mycursor.rowcount,"inserted")
    else :
        print("pressed wrong key")
        continue
    

