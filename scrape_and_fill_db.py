import sqlite3
import time
import undetected_chromedriver as uc

import webscrape


class ScrapeAndFillDB:
    def __init__(self):
        self.chromeOptions = uc.ChromeOptions().add_argument('--headless')
        self.driver = uc.Chrome()
        self.webscrape = webscrape.WebScrape()

    def scrape_all_time(self):
        page = 13444
        driver = uc.Chrome()
        table_name: str = 'lotto_numbers'
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
            # time.sleep(random.randint(1, 3))
            print(f'page: {page}')
            sql = f'''INSERT INTO {table_name} ('page', 'date', 'day_of_week', 'time_of_day', 'first', 'second',
            'third', 'fourth', 'fifth') VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);'''
            param_list = [(page, date, day_of_week, time_of_day, first, second, third, fourth, fifth)]
            cursor.executemany(sql, param_list)

            connection.commit()
            page = page - 1

    def create_table(self, table_name):
        connection = sqlite3.connect(table_name, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        sql_table = f''' CREATE TABLE IF NOT EXISTS {table_name} (
                        page integer PRIMARY KEY,
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
        connection.commit()
        connection.close()


def main():
    daily_scraper = ScrapeAndFillDB()
    daily_scraper.scrape_all_time()


if __name__ == '__main__':
    main()
