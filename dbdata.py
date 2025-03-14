# tu wstawimy dane startowe w każdą z tabel sql

# spis tabel

# bank
# daily
# dron
# learning
# shopping
# work


import sqlite3

# przyklad
import mysql.connector

# baza
db_host = 'localhost'
db_name = 'startsite_db'
db_user = 'root'
db_pass = 'egon'

my_db = mysql.connector.connect(host = db_host,  user=db_user, password=db_pass, database=db_name)
# bank
mycursor = my_db.cursor()
mycursor.execute("INSERT INTO `startsite_db`.`bank` (`id`, `name`, `adress`) VALUES ('1', 'bank1 ', 'www Adres bank1')")
