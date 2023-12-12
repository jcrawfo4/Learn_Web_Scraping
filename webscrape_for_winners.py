import sqlite3

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import undetected_chromedriver as uc


class WebScrapeForWinners:
    def __init__(self):
        self.table_name = "winners"
        self.driver = uc.Chrome(headless=True, use_subprocess=False)
        self.wait = WebDriverWait(self.driver, 8)

    def create_table(self):
        connection = sqlite3.connect(self.table_name, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        sql_table = f''' CREATE TABLE IF NOT EXISTS {self.table_name} (
                        page integer PRIMARY KEY,
                        date text NOT NULL,
                        winner integer NOT NULL,
                        jackpot integer NOT NULL,
                        four_fifth integer NOT NULL,
                        three_fifth integer NOT NULL,
                        two_fifth integer NOT NULL
                    ); '''
        cursor = connection.cursor()
        cursor.execute(sql_table)
        connection.commit()
        connection.close()

    def scrape(self):
        connection = sqlite3.connect('winners', timeout=10,
                                     detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        cursor = connection.cursor()

        for page in range(14325, 14335):
            print("page: ", page)
            self.driver.get(f"https://www.illinoislottery.com/dbg/results/luckydaylotto/draw/{page}")

            winner = self.get_winner()

            jackpot = self.get_jackpot()

            date = self.get_date()

            four_fifth = self.get_four_fifths()

            three_fifth = self.get_three_fifths()

            two_fifth = self.get_two_fifths()

            self.print_win_related(page, date, winner, jackpot)
            self.print_fifths(four_fifth, three_fifth, two_fifth)

            sql = f'''INSERT INTO {self.table_name}  ('page', 'date', 'winner', 'jackpot', 'four_fifth', 'three_fifth',
                'two_fifth') VALUES (?, ?, ?, ?, ?, ?, ?);'''

            param_list = [(page, date, winner, jackpot, four_fifth,
                           three_fifth, two_fifth)]

            cursor.executemany(sql, param_list)
            connection.commit()
            connection.close()

    def print_win_related(self, page, date, winner, jackpot):
        print("page: ", page, "date: ", str(date), "winner? : ", str(winner), "jackpot ", str(jackpot))

    def print_fifths(self, four_fifth, three_fifth, two_fifth):
        print("4/5: ", four_fifth, "3/5: ", three_fifth, "2/5: ", two_fifth)

    def get_date(self):
        date_element = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/main/div[2]/div[2]/div/section/div/time/span[2]')))
        date = date_element.text
        return date

    def get_two_fifths(self):
        two_fifth_element = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/main/div[2]/div[2]/div/section/div/section/table/tbody/tr[4]/td[3]')))
        two_fifth = int(two_fifth_element.text)
        return two_fifth

    def get_three_fifths(self):
        three_fifth_element = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/main/div[2]/div[2]/div/section/div/section/table/tbody/tr[3]/td[3]')))
        three_fifth = int(three_fifth_element.text)
        return three_fifth

    def get_four_fifths(self):
        four_fifth_element = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/main/div[2]/div[2]/div/section/div/section/table/tbody/tr[2]/td[3]')))
        four_fifth = int(four_fifth_element.text)
        return four_fifth

    def get_jackpot(self):

        jackpot_element = self.wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div[2]/div['
                                                                                   '2]/div/section/div/section'
                                                                                   '/table/tbody/tr[1]/td[2]/div')))
        jackpot_input: str = jackpot_element.text
        # Remove all non-digit characters
        stripped_string = ''.join(filter(str.isdigit, jackpot_input))
        if "." in jackpot_input:  # Convert the stripped string to an integer
            jackpot = int(stripped_string[:-2])
        else:
            jackpot = stripped_string
        return jackpot

    def get_winner(self):
        winner_element = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="il-web-app"]/div[2]/div[2]/div/section/div/section/table/tbody/tr[1]/td[3]')))
        # Retrieve the element's value or text
        winner = int(winner_element.text)
        return winner


def main():
    scraper = WebScrapeForWinners()
    scraper.create_table()
    scraper.scrape()


if __name__ == '__main__':
    main()
