import random
import sqlite3
import time

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from sqlite3 import Error


class Webscrape:
    def __init__(self) -> object:
        self.chrome_options = uc.ChromeOptions().add_argument('--headless')
        self.driver = uc.Chrome(self.chrome_options)

    def scrape(self):
        page = 13444
        driver = uc.Chrome()
        table_name = 'lottery.db'
        self.create_table(table_name)
        for i in reversed(range(10)):
            url: str = f'https://www.illinoislottery.com/dbg/results/luckydaylotto/draw/{page}'
            driver.get(url)
            day_of_week: str = str(self.get_day_of_week(driver))
            date = self.get_date(driver)
            time_of_day = self.get_time_of_day()
            first: str = self.get_first(driver)
            second = self.get_second(driver)
            third = self.get_third(driver)
            fourth = self.get_fourth(driver)
            fifth = self.get_fifth(driver)
            data_string = f'({date}, {day_of_week}, {time_of_day}, {first}, {second}, {third}, {fourth}, {fifth})'
            self.make_entry('lottery.db', data_string)
            self.print_stuff(date, day_of_week, time_of_day)
            self.print_balls(first, second, third, fourth, fifth)
            page = page - 1
            time.sleep(random.randint(2, 6))

    def get_date(self, driver):
        date = driver.find_element(By.XPATH,
                                   '//*[@id="il-web-app"]/div[2]/div[2]/div/section/div/time/span[2]')
        return date

    def get_day_of_week(self, driver):
        day_of_week = driver.find_element(By.XPATH, '//*[@id="il-web-app"]/div[2]/div[2]/div/section/div/time/span[4]')
        return str(day_of_week)

    def get_time_of_day(driver):
        time_of_day = driver.find_element(By.CSS_SELECTOR,
                                          '#il-web-app > div.book-container.book-container--luckydaylotto > '
                                          'div.exc-container.exc-container__body.exc-container--with-bottom-margin.book'
                                          '-container__content > div > section > div > time > '
                                          'span.dbg-result-details__draw-phase')
        return str(time_of_day)

    def get_first(self, driver):
        first = driver.find_element(By.ID, "result-line-primary-0-selected")
        return first

    def get_second(self, driver):
        second = driver.find_element(By.ID, 'result-line-primary-1-selected')
        return second

    def get_third(self, driver):
        third = driver.find_element(By.ID, 'result-line-primary-2-selected')
        return third

    def get_fourth(self, driver):
        fourth = driver.find_element(By.ID, "result-line-primary-3-selected")
        return fourth

    def get_fifth(self, driver):
        fifth = driver.find_element(By.ID, "result-line-primary-4-selected")
        return fifth

    def print_stuff(self, date, day_of_week, time_of_day):
        print("Day of the week: ", day_of_week.text)
        print("Date: ", date.text)
        print("Time of day: ", time_of_day.text)

    def print_balls(self, first, second, third, fourth, fifth):
        print("First: ", first.text)
        print("Second: ", second.text)
        print("Third: ", third.text)
        print("Fourth: ", fourth.text)
        print("Fifth: ", fifth.text)

    def create_connection(db_file):
        """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)

        return conn

        def create_connection(self, db_file):
            """ create a database connection to the SQLite database
                specified by db_file
            :param db_file: database file
            :return: Connection object or None
            """
            try:
                self.conn = sqlite3.connect(db_file)
                cur = self.conn.cursor()
                return cur
            except Error as e:
                print(e)

        def create_table(self, table_name):
            sql = f''' CREATE TABLE IF NOT EXISTS {table_name} (
                        id integer PRIMARY KEY,
                        date text NOT NULL,
                        day_of_week text NOT NULL,
                        time_of_day text NOT NULL,
                        first integer NOT NULL,
                        second integer NOT NULL,
                        third integer NOT NULL,
                        fourth integer NOT NULL,
                        fifth integer NOT NULL
                    ); '''
            cur = self.create_connection('lotto_numbers')
            cur.execute(sql)
            self.conn.commit()

        def make_entry(self, table_name):
            sql_insert = ''' INSERT INTO $table_name(date, day_of_week, time_of_day, first, second, third, fourth, fifth)
                      VALUES(?, ?, ?, ?, ?, ?, ?, ?);'''
            cur = self.create_connection('lotto_numbers')
            cur.execute(sql_insert)
            self.conn.commit()
            return cur.lastrowid

        def close_connection(self):
            self.conn.close()

        def get_all_entries(self, table_name):
            cur = self.create_connection('lotto_numbers')
            cur.execute(f'SELECT * FROM {table_name} limit 10')
            rows = cur.fetchall()
            for row in rows:
                print(row)


if __name__ == '__main__':
    ws = Webscrape()
    ws.scrape()
