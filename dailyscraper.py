import time
from datetime import date

import undetected_chromedriver as uc

import webscrape

import threading as th


class DailyScraper:
    def __init__(self):
        pass
        # self.chromeOptions = uc.ChromeOptions().add_argument('--headless')
        # self.driver = uc.Chrome()
        # self.webscrape = webscrape.WebScrape()

    def countdown(self):
        time.sleep(24)
        print("stopped countdown()")

    def print_hello(self):
        print("hello world")

    def get_last_page(self):
        page = f'SELECT MAX(page) FROM lotto_numbers.db'


    # def scrape(self):
    #     page = 13444
    #     table_name = 'lotto_numbers'
    #     self.driver.get('https://www.illinoislottery.com/account/login')
    #
    # def get_todays_date(self):
    #     today = date.today()
    #     # Textual month, day and year
    #     d2 = today.strftime("%B %d, %Y")
    #     print("d2 =", d2)
    #     return d2


def print_hello():
    print("hello world")


def main():
    daily_scraper = DailyScraper()
    daily_scraper.countdown()


if __name__ == '__main__':
    main()
