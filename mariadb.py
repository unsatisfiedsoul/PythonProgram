#! bin/python3
import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="rony",
	password="766900"

)
#print(mydb)

mycursor = mydb.cursor()

mycursor.execute("create database if not exists pythonDB")
mycursor.execute("show databases")

for x in mycursor:
	print(x)

mycursor.execute("use pythonDB")

mycursor.execute('create table if not exists users(id int not null auto_increment,name varchar(100) not null, password varchar(100) not null, primary key (id))')

print("-------------------------")
mycursor.execute("show tables")
for x in mycursor:
	print(x)
