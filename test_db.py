import mysql.connector
mydb = mysql.connector.connect(user='root', password='adminadmin',
                             host='127.0.0.1', database='db_control')
print(mydb)