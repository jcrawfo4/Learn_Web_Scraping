import random
import time

from webscrape import WebScrape


class ScrapeAndFillDB:
    def __init__(self):
        self.table = 'lotto_numbers'
        self.webscrape = WebScrape()

    def scrape_all_time(self, webscrape):
        while True:
            time.sleep(random.randint(0, 3))
            webscrape.daily_scrape()


def main():
    scrape_and_fill_db = ScrapeAndFillDB()
    scrape_and_fill_db.scrape_all_time(scrape_and_fill_db.webscrape)


if __name__ == '__main__':
    main()
