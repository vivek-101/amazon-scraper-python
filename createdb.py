import mysql.connector

myDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    auth_plugin='mysql_native_password',
)

myCursor = myDB.cursor()
myCursor.execute("CREATE DATABASE ciqDB")
myCursor.execute("CREATE TABLE product(productId varchar(40), productTitle varchar(100), productPrice float(10,2), productDescription(200), ")
