# pokaż  dane z  bazy
from pydoc import importfile

# importfile('db_config.py')

import json
import mysql.connector
# baza
db_host = 'localhost'
db_name = 'startsite_db'
db_user = 'root'
db_pass = 'egon'

my_db = mysql.connector.connect(host = db_host,  user=db_user, password=db_pass, database=db_name)

mycursor = my_db.cursor()

mycursor.execute("select * from shopping")

for i in mycursor:
    json_output = json.dumps(i)
    print(json_output)
