import mysql.connector 

database = mysql.connector.connect(
    username = 'root',
    passwd = '1234',
    host= 'localhost',

)
# prepar the cursor object
cursorObject = database.cursor()

# creat database
cursorObject.execute("CREATE DATABASE yassin")
print('All Done!')