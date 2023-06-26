
# Import required modules
import csv
import sqlite3

# Connecting to the lotto database
connection = sqlite3.connect('lotto_results.db')

# Creating a cursor object to execute
# SQL queries on a database table
cursor = connection.cursor()

# Table Definition
create_table = '''CREATE TABLE lotto_table(
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				first integer NOT NULL,
				second INTEGER NOT NULL,
				third INTEGER NOT NULL, 
				fourth INTEGER NOT NULL,
				fifth INTEGER NOT NULL);
				'''

# Creating the table into our
# database
cursor.execute(create_table)

# Opening the person-records.csv file
file = open('lotto_results_trial.txt')

# Reading the contents of the
# person-records.csv file
contents = csv.reader(file)

# SQL query to insert data into the
# person table
insert_records = "INSERT INTO lotto_table (first, second, third, fourth, fifth) VALUES(?, ?, ?, ?, ?)"

# Importing the contents of the file
# into our lotto table
cursor.executemany(insert_records, contents)

# SQL query to retrieve all data from
# the person table To verify that the
# data of the csv file has been successfully
# inserted into the table
select_all = "SELECT * FROM lotto_table"
rows = cursor.execute(select_all).fetchall()

# Output to the console screen
for r in rows:
	print(r)

# Committing the changes
connection.commit()

# closing the database connection
connection.close()
