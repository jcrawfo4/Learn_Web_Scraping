import random
import sqlite3
import time

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By


def scrape():
    page = 13444
    driver = uc.Chrome()
    table_name = 'lotto_numbers'
    create_table(table_name, )
    for i in reversed(range(10)):
        url: str = f'https://www.illinoislottery.com/dbg/results/luckydaylotto/draw/{page}'
        driver.get(url)
        day_of_week: str = str(get_day_of_week(driver))
        date = get_date(driver)
        time_of_day = get_time_of_day(driver)
        first_ball = get_first(driver)
        second = get_second(driver)
        third = get_third(driver)
        fourth = get_fourth(driver)
        fifth = get_fifth(driver)

        print_stuff(date, day_of_week, time_of_day)
        print_balls(first_ball, second, third, fourth, fifth)
        page = page - 1
        table_name = 'lotto_numbers'
        time.sleep(random.randint(2, 6))
        sql_one = "INSERT INTO lotto_numbers (date, day_of_week, time_of_day, first_ball, second, third, fourth, fifth"
        sql_two: str = f"VALUES {date}, {day_of_week}, {time_of_day}, {first_ball}, {second}, {third}, {fourth}, {fifth};"
        sql_insert: str = sql_one + sql_two

        connection = sqlite3.connect('lotto_numbers.db')
        cursor = connection.cursor()
        cursor.execute(sql_insert)
        connection.commit()


def get_date(driver):
    date = driver.find_element(By.XPATH,
                               '//*[@id="il-web-app"]/div[2]/div[2]/div/section/div/time/span[2]')
    return str(date.text)


def get_day_of_week(driver):
    day_of_week = driver.find_element(By.XPATH, '//*[@id="il-web-app"]/div[2]/div[2]/div/section/div/time/span[4]')
    return str(day_of_week.text)


def get_time_of_day(driver):
    time_of_day = driver.find_element(By.CSS_SELECTOR,
                                      '#il-web-app > div.book-container.book-container--luckydaylotto > '
                                      'div.exc-container.exc-container__body.exc-container--with-bottom-margin.book'
                                      '-container__content > div > section > div > time > '
                                      'span.dbg-result-details__draw-phase')
    return str(time_of_day.text)


def get_first(driver):
    first = driver.find_element(By.ID, "result-line-primary-0-selected")
    return first.text


def get_second(driver):
    second = driver.find_element(By.ID, 'result-line-primary-1-selected')
    return second.text


def get_third(driver):
    third = driver.find_element(By.ID, 'result-line-primary-2-selected')
    return third.text


def get_fourth(driver):
    fourth = driver.find_element(By.ID, "result-line-primary-3-selected")
    return fourth.text


def get_fifth(driver):
    fifth = driver.find_element(By.ID, "result-line-primary-4-selected")
    return fifth.text


def print_stuff(date, day_of_week, time_of_day):
    print("Day of the week: ", day_of_week)
    print("Date: ", date)
    print("Time of day: ", time_of_day)


def print_balls(first, second, third, fourth, fifth):
    print("First: ", first)
    print("Second: ", second)
    print("Third: ", third)
    print("Fourth: ", fourth)
    print("Fifth: ", fifth)


def create_table(table_name):
    sql = f''' CREATE TABLE IF NOT EXISTS lotto_numbers (
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
    connection = sqlite3.connect('lotto_numbers.db')
    cursor = connection.cursor()
    cursor.execute(sql)


# def make_entry(date, day_of_week, time_of_day, first, second, third, fourth, fifth):
#     table_name = 'lotto_numbers'
#     sql_insert = ''' INSERT INTO $table_name(date, day_of_week, time_of_day, first, second, third, fourth, fifth)
#                   VALUES(?, ?, ?, ?, ?, ?, ?, ?);'''
#     data_tuple = (date, day_of_week, time_of_day, first, second, third, fourth, fifth)
#     connection = sqlite3.connect('lotto_numbers.db')
#     cursor = connection.cursor()
#     cursor.execute(sql_insert, data_tuple)
#     return cursor.lastrowid


def close_connection(conn):
    conn.close()


def get_all_entries(table_name):
    connection = sqlite3.connect('lotto_numbers')
    cur = connection.cursor()
    cur.execute(f'SELECT * FROM {table_name} limit 10')
    rows = cur.fetchall()
    for row in rows:
        print(row)


scrape()
