import sqlite3

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from undetected_chromedriver import Chrome


def create_table(table_name):
    connection = sqlite3.connect(table_name, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    sql_table = f''' CREATE TABLE IF NOT EXISTS {table_name} (
                    page integer PRIMARY KEY,
                    date text NOT NULL,
                    winner integer NOT NULL,
                    jackpot integer NOT NULL,
                    four_fifth text NOT NULL,
                    three_fifth integer NOT NULL,
                    two_fifth integer NOT NULL
                ); '''
    cursor = connection.cursor()
    cursor.execute(sql_table)
    connection.commit()
    connection.close()


def scrape():
    global page, wait, winner_element
    with Chrome() as driver:
        table_name = 'winners'

        connection = sqlite3.connect("winners", timeout=10,
                                     detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        cursor = connection.cursor()

        for page in range(7112, 7222):
            driver.get(f"https://www.illinoislottery.com/dbg/results/luckydaylotto/draw/{page}")
            # Use WebDriverWait to wait for the element to be present
            winner = get_winner(driver)

            wait_two = WebDriverWait(driver, 3)
            jackpot_element = wait_two.until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div[2]/div['
                                                                                       '2]/div/section/div/section'
                                                                                       '/table/tbody/tr[1]/td[2]/div')))
            jackpot: object = jackpot_element.text

            wait_three = WebDriverWait(driver, 3)
            date_element = wait_three.until(EC.presence_of_element_located(
                (By.XPATH, '/html/body/main/div[2]/div[2]/div/section/div/time/span[2]')))
            date = date_element.text

            wait_four = WebDriverWait(driver, 3)

            four_fifth_element = wait_four.until(EC.presence_of_element_located(
                (By.XPATH, '/html/body/main/div[2]/div[2]/div/section/div/section/table/tbody/tr[2]/td[3]')))
            four_fifth = four_fifth_element.text

            wait_five = WebDriverWait(driver, 3)
            three_fifth_element = wait_five.until(EC.presence_of_element_located(
                (By.XPATH, '/html/body/main/div[2]/div[2]/div/section/div/section/table/tbody/tr[3]/td[3]')))
            three_fifth = three_fifth_element.text

            wait_six = WebDriverWait(driver, 3)
            two_fifth_element = wait_six.until(EC.presence_of_element_located(
                (By.XPATH, '/html/body/main/div[2]/div[2]/div/section/div/section/table/tbody/tr[4]/td[3]')))
            two_fifth = two_fifth_element.text
            print("page: ", page, "date: ", date, "winner? : ", winner, "jackpot amount: ", jackpot, "four_fifth: ", four_fifth, "three_fifths: ", three_fifth, "two_fifths: ", two_fifth)

            sql = f'''INSERT INTO {table_name} ('page', 'date', 'winner', 'jackpot', 'four_fifth', 'three_fifth', 'two_fifth') VALUES (?, ?, ?, ?, ?, ?, ?);'''
            param_list = [page, date, winner, jackpot, four_fifth, three_fifth, two_fifth]
            # Check the value of the 'winner' column before inserting it.

            # Insert the data into the table.
            cursor.executemany(sql, param_list)
            connection.commit()
            connection.close()


def get_winner(driver):
    global wait, winner_element
    wait = WebDriverWait(driver, 3)  # Adjust the timeout as needed
    winner_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="il-web-app"]/div[2]/div['
                                                                          '2]/div/section/div/section/table'
                                                                          '/tbody/tr['
                                                                          '1]/td['
                                                                          '3]')))
    # Retrieve the element's value or text
    winner = winner_element.text
    return winner


#create_table('winners')
scrape()
