import sqlite3
from sqlite3 import Error


# def create_connection(db_file):
#     """ create a database connection to the SQLite database
#         specified by db_file
#     :param db_file: database file
#     :return: Connection object or None
#     """
#     conn = None
#     try:
#         conn = sqlite3.connect(db_file)
#     except Error as e:
#         print(e)
#
#     return conn
#
#
# class DbHandler:
#
#     def __init__(self):
#         self.conn = None
#
#     def create_connection(self, db_file):
#         """ create a database connection to the SQLite database
#             specified by db_file
#         :param db_file: database file
#         :return: Connection object or None
#         """
#         try:
#             self.conn = sqlite3.connect(db_file)
#             cur = self.conn.cursor()
#             return cur
#         except Error as e:
#             print(e)
#
#     def create_table(self, table_name):
#         sql = f''' CREATE TABLE IF NOT EXISTS {table_name} (
#                     id integer PRIMARY KEY,
#                     date text NOT NULL,
#                     day_of_week text NOT NULL,
#                     time_of_day text NOT NULL,
#                     first integer NOT NULL,
#                     second integer NOT NULL,
#                     third integer NOT NULL,
#                     fourth integer NOT NULL,
#                     fifth integer NOT NULL
#                 ); '''
#         cur = self.create_connection('lotto_numbers')
#         cur.execute(sql)
#         self.conn.commit()
#
#     def make_entry(self, table_name):
#         sql_insert = ''' INSERT INTO $table_name(date, day_of_week, time_of_day, first, second, third, fourth, fifth)
#                   VALUES(?, ?, ?, ?, ?, ?, ?, ?);'''
#         cur = self.create_connection('lotto_numbers')
#         cur.execute(sql_insert)
#         self.conn.commit()
#         return cur.lastrowid
#
#     def close_connection(self):
#         self.conn.close()
#
#     def get_all_entries(self, table_name):
#         cur = self.create_connection('lotto_numbers')
#         cur.execute(f'SELECT * FROM {table_name} limit 10')
#         rows = cur.fetchall()
#         for row in rows:
#             print(row)