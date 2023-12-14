import random
import sqlite3
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By


class WebScrape:

    def __init__(self):
        self.driver = Chrome(use_subprocess=True)
        self.table_name = 'lotto_numbers'
        self.wait = WebDriverWait(self.driver, 8)

    def daily_scrape(self):

        for page in range(14326, 14344):
            try:
                table_name = 'lotto_numbers'
                connection = sqlite3.connect(table_name, timeout=10,
                                             detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
                cursor = connection.cursor()
                # page = self.get_last_page()
                time.sleep(random.randint(0, 3))
                url = f'https://www.illinoislottery.com/dbg/results/luckydaylotto/draw/{page}'
                self.driver.get(url)
                date = self.get_date(self.driver)
                day_of_week = self.get_day_of_week(self.driver)
                time_of_day = self.get_time_of_day(self.driver)
                first = self.get_first(self.driver)
                second = self.get_second(self.driver)
                third = self.get_third(self.driver)
                fourth = self.get_fourth(self.driver)
                fifth = self.get_fifth(self.driver)
                sql = f'''INSERT INTO {table_name} ('page', 'date', 'day_of_week', 'time_of_day', 'first', 'second',
                'third', 'fourth', 'fifth') VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);'''
                param_list = [(page, date, day_of_week, time_of_day, first, second, third, fourth, fifth)]
                cursor.executemany(sql, param_list)
                # self.driver.quit()
                connection.commit()
                # connection.close()

            except sqlite3.IntegrityError:
                print("IntegrityError")

    def get_last_page(self):
        try:
            page_query = f'''SELECT MAX(page) FROM {self.table_name}'''
            connection = sqlite3.connect('../lotto_numbers',
                                         detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            cursor = connection.cursor()
            page = cursor.execute(page_query).fetchone()[0]
            print("page: ", page)
            connection.commit()
            connection.close()
            if page is None:
                print("cursor.execute(page_query).fetchone()[0] FAILED !!!")
                return
            else:
                return page
        except sqlite3.OperationalError:
            print("OperationalError page not found")

    def get_date(self, d) -> str:
        date = d.find_element(By.XPATH, '//*[@id="il-web-app"]/div[2]/div[2]/div/section/div/time/span[2]')
        return str(date.text.strip()).strip()

    def get_day_of_week(self, d):
        day_of_week = d.find_element(By.XPATH, '//*[@id="il-web-app"]/div[2]/div[2]/div/section/div/time/span[1]')
        day_of_week = str(day_of_week.text.strip())[0:-1]
        return day_of_week.strip()

    def get_time_of_day(self, d):
        time_of_day = d.find_element(By.XPATH,
                                     '//*[@id="il-web-app"]/div[2]/div[2]/div/section/div/time/span[4]')
        return str(time_of_day.text.strip()).strip()

    def get_first(self, driver):
        first = driver.find_element(By.ID, "result-line-primary-0-selected")
        return str(first.text).strip()

    def get_second(self, driver):
        second = driver.find_element(By.ID, 'result-line-primary-1-selected')
        return str(second.text).strip()

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

    # def get_all_entries(self, table_name):
    #     connection = sqlite3.connect(table_name, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    #     cur = connection.cursor()
    #     cur.execute(f'SELECT * FROM {table_name} limit 7')
    #     rows = cur.fetchall()
    #     print("calling get_all_entries")
    #     for row in rows:
    #         print(row)
    #     connection.close()

    # scrape_all_time() scrapes all the pages from the website and stores them in a database


def main():
    scraper = WebScrape()
    scraper.daily_scrape()


if __name__ == '__main__':
    main()
