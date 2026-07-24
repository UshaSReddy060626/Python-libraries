#import library
import sqlite3
#create database
connection = sqlite3.connect("students.db")
#create cursor
cursor = connection.cursor()
#create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    name TEXT,
    age INTEGER)""")
#insert data
cursor.execute(
    "INSERT INTO students VALUES(?, ?)",
    ("Usha", 21)
)
#save changes
connection.commit()
#read data
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
print(rows)
#close database
connection.close()