import random
import sqlite3
import time

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By


class WebScrape:
    def __init__(self):
        self.chromeOptions = uc.ChromeOptions().add_argument('--headless')
        self.driver = uc.Chrome()

    def daily_scrape(self, date, day_of_week, time_of_day, first, second, third, fourth, fifth):
        table_name = 'lotto_numbers'
        self.create_table(table_name)
        connection = sqlite3.connect(table_name, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        cursor = connection.cursor()
        sql = f'''INSERT INTO {table_name} ('date', 'day_of_week', 'time_of_day', 'first', 'second',
        'third', 'fourth', 'fifth') VALUES (?, ?, ?, ?, ?, ?, ?, ?);'''
        param_list = [(date, day_of_week, time_of_day, first, second, third, fourth, fifth)]
        cursor.executemany(sql, param_list)
        connection.commit()
    def scrape_all_time(self):
        page = 13444
        driver = uc.Chrome()
        table_name = 'lotto_numbers'
        self.create_table(table_name)
        connection = sqlite3.connect(table_name, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        cursor = connection.cursor()
        for i in reversed(range(100)):
            url: str = f'https://www.illinoislottery.com/dbg/results/luckydaylotto/draw/{page}'
            driver.get(url)
            date = self.get_date(driver)
            day_of_week = self.get_day_of_week(driver)
            time_of_day = self.get_time_of_day(driver)
            first = self.get_first(driver)
            second = self.get_second(driver)
            third = self.get_third(driver)
            fourth = self.get_fourth(driver)
            fifth = self.get_fifth(driver)

            self.print_stuff(date, day_of_week, time_of_day)
            self.print_balls(first, second, third, fourth, fifth)
            time.sleep(random.randint(1, 6))
            sql = f'''INSERT INTO {table_name} ('date', 'day_of_week', 'time_of_day', 'first', 'second',
            'third', 'fourth', 'fifth') VALUES (?, ?, ?, ?, ?, ?, ?, ?);'''
            param_list = [(date, day_of_week, time_of_day, first, second, third, fourth, fifth)]
            cursor.executemany(sql, param_list)

            connection.commit()
            page = page - 1

    def get_date(self, driver):
        date = driver.find_element(By.XPATH,
                                   '//*[@id="il-web-app"]/div[2]/div[2]/div/section/div/time/span[2]')
        return str(date.text)

    def get_day_of_week(self, driver):
        day_of_week = driver.find_element(By.XPATH, '//*[@id="il-web-app"]/div[2]/div[2]/div/section/div/time/span[1]')
        day_of_week = str(day_of_week.text)[0:-1]
        return day_of_week

    def get_time_of_day(self, driver):
        time_of_day = driver.find_element(By.CSS_SELECTOR,
                                          '#il-web-app > div.book-container.book-container--luckydaylotto > '
                                          'div.exc-container.exc-container__body.exc-container--with-bottom-margin.book'
                                          '-container__content > div > section > div > time > '
                                          'span.dbg-result-details__draw-phase')
        return str(time_of_day.text)

    def get_first(self, driver):
        first = driver.find_element(By.ID, "result-line-primary-0-selected")
        return str(first.text)

    def get_second(self, driver):
        second = driver.find_element(By.ID, 'result-line-primary-1-selected')
        return str(second.text)

    def get_third(self, driver):
        third = driver.find_element(By.ID, 'result-line-primary-2-selected')
        return str(third.text)

    def get_fourth(self, driver):
        fourth = driver.find_element(By.ID, "result-line-primary-3-selected")
        return str(fourth.text)

    def get_fifth(self, driver):
        fifth = driver.find_element(By.ID, "result-line-primary-4-selected")
        return str(fifth.text)

    def print_stuff(self, date, day_of_week, time_of_day):
        print("Date: " + date)
        print("Day of the week: " + day_of_week)
        print("Time of day: " + time_of_day)

    def print_balls(self, first, second, third, fourth, fifth):
        print("First: " + first)
        print("Second: " + second)
        print("Third: " + third)
        print("Fourth: " + fourth)
        print("Fifth: " + fifth)

    def create_table(self, table_name):
        connection = sqlite3.connect(table_name)
        sql_table = f''' CREATE TABLE IF NOT EXISTS {table_name} (
                        date text NOT NULL,
                        day_of_week text NOT NULL,
                        time_of_day text NOT NULL,
                        first integer NOT NULL,
                        second integer NOT NULL,
                        third integer NOT NULL,
                        fourth integer NOT NULL,
                        fifth integer NOT NULL
                    ); '''
        cursor = connection.cursor()
        cursor.execute(sql_table)

    # def make_entry(self, table_name, page, date, day_of_week, time_of_day, first, second, third, fourth, fifth):
    #     sql = f'''INSERT INTO {table_name} ('page','date', 'day_of_week', 'time_of_day', 'first', 'second',
    #     'third', 'fourth', 'fifth') VALUES (?,?, ?, ?, ?, ?, ?, ?, ?);'''
    #     param_list = [(page, date, day_of_week, time_of_day, first, second, third, fourth, fifth)]
    #     return sql, param_list

    def close_connection(self, conn):
        conn.close()

    def get_all_entries(self, table_name):
        connection = sqlite3.connect(table_name, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        cur = connection.cursor()
        cur.execute(f'SELECT * FROM {table_name} limit 10')
        rows = cur.fetchall()
        for row in rows:
            print(row)

    # scrape_all_time() scrapes all the pages from the website and stores them in a database


def main():
    scraper = WebScrape()
    scraper.scrape_all_time()


if __name__ == '__main__':
    main()
