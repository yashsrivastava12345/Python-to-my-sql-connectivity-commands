import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="yash 12345 yash @",database="school2")
mycursor=mydb.cursor()
i=0
# while True:
    cho=input("Enter your choice\n q to quit \n n for resuming to enter data\n: ")
    if cho=="Q" or cho=="q":
        break
    elif cho=="N" or cho=="n":
        a=int(input("Enter roll number: "))
        b=input("Enter name: ")
        c=int(input("Enter age:"))
        d=input ("Enter class: ")
        e=input("Enter city: ")
        sql="insert into student(rollno,name,age,class,city) values (%s,%s,%s,%s,%s)"
        val=(a,b,c,d,e)
        mycursor.execute(sql,val)
        mydb.commit()
        print(mycursor.rowcount,"inserted")
    else :
        print("pressed wrong key")
        continue
    

