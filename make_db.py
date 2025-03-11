# tworzymy tabele w sql i bawimy się
import sqlite3

# przyklad
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="egon",
)
#W   database="startsite_db"

mycursor = mydb.cursor()
# tworzymy bazę
mycursor.execute("CREATE DATABASE IF NOT EXISTS startsite_db")

# a w niej tabele

mycursor = mydb.cursor()
mycursor.execute("USE startsite_db")
sql_work = """
    CREATE TABLE IF NOT EXISTS work (
      `id` int NOT NULL,
      `name` varchar(45) NOT NULL,
      `adress` varchar(45) NOT NULL,
      `description` varchar(45) DEFAULT NULL,
      PRIMARY KEY (`id`)
    )
    """
mycursor.execute(sql_work)

sql_bank = """
 CREATE TABLE IF NOT EXISTS bank (
      `id` int NOT NULL,
      `name` varchar(45) NOT NULL,
      `adress` varchar(45) NOT NULL,
      `description` varchar(45) DEFAULT NULL,
      PRIMARY KEY (`id`)
  )
  """
mycursor.execute(sql_bank)

sql_dron = """
 CREATE TABLE IF NOT EXISTS dron (
      `id` int NOT NULL,
      `name` varchar(45) NOT NULL,
      `adress` varchar(45) NOT NULL,
      `description` varchar(45) DEFAULT NULL,
      PRIMARY KEY (`id`)
  )
  """
mycursor.execute(sql_dron)

sql_daily = """
 CREATE TABLE IF NOT EXISTS daily (
      `id` int NOT NULL,
      `name` varchar(45) NOT NULL,
      `adress` varchar(45) NOT NULL,
      `description` varchar(45) DEFAULT NULL,
      PRIMARY KEY (`id`)
  )
  """
mycursor.execute(sql_daily)

sql_learning = """
 CREATE TABLE IF NOT EXISTS learning (
      `id` int NOT NULL,
      `name` varchar(45) NOT NULL,
      `adress` varchar(45) NOT NULL,
      `description` varchar(45) DEFAULT NULL,
      PRIMARY KEY (`id`)
  )
  """
mycursor.execute(sql_learning)

sql_shopping = """
 CREATE TABLE IF NOT EXISTS shopping (
      `id` int NOT NULL,
      `name` varchar(45) NOT NULL,
      `adress` varchar(45) NOT NULL,
      `description` varchar(45) DEFAULT NULL,
      PRIMARY KEY (`id`)
  )
  """
mycursor.execute(sql_shopping)

