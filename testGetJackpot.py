import sqlite3

import sqlite3
conn = sqlite3.connect('lotto_numbers')
conn.execute("CREATE TABLE IF NOT EXISTS lotto_numbers (id int, description text)")
conn.execute("INSERT INTO lotto_numbers VALUES (1, 'test')")
conn.commit()