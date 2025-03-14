import mysql.connector
# baza
db_host = 'localhost'
db_name = 'moja_db1'
db_user = 'root'
db_pass = 'egon'

my_db = mysql.connector.connect(host = db_host,  user=db_user, password=db_pass, database=db_name)

mycursor = my_db.cursor()