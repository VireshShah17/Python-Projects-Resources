import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",passwd="123456",auth_plugin='mysql_native_password',database="foodzone")
if mycon.is_connected():
    print("Database Connection Successful")
else:
    print("Database Connection Error")
cursor=mycon.cursor()
tablesql='''CREATE TABLE ulogin(
MobileNo varchar(10) primary key,
Name varchar(50) NOT NULL,
DOB date,
State varchar(20) NOT NULL,
Favourite_FoodDish varchar(30));'''
cursor.execute(tablesql)
mycon.close()