#!bin/python3

import mysql.connector
import hashlib

def calculate_sha256(data):
	if isinstance(data,str):
		data = data.encode()
		sha256_hash = hashlib.sha256(data).hexdigest()
	return sha256_hash


username = input("What is your username: ")
password = input("What is your password: ")

hash_value = calculate_sha256(password)

mydb = mysql.connector.connect(
	host = "localhost",
	user = "rony",
	password = "766900",
	database = "pythonDB"
)

mycursor = mydb.cursor()

sql = "insert into users(name,password) values(%s,%s)"
val = (username,hash_value)
mycursor.execute(sql,val)

mydb.commit()

print(mycursor.rowcount,"record inserted.")
