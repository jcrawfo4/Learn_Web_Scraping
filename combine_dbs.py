import sqlite3

# Connect to both databases
conn1 = sqlite3.connect('lotto_numbers')
conn2 = sqlite3.connect('winners')

# Create a new database or connect to an existing one
new_db_conn = sqlite3.connect('winners')
cursor1 = conn1.cursor()
cursor2 = conn2.cursor()
new_cursor = new_db_conn.cursor()

# Copy data from the first database to the new database
cursor1.execute('ATTACH DATABASE "winners" AS db2')
new_cursor.execute('CREATE TABLE combined_table AS SELECT * FROM main_table JOIN db2.attached_table ON main_table.id = db2.attached_table.id')

# Commit and close the connections
new_db_conn.commit()
new_db_conn.close()
conn1.close()
conn2.close()
