import random
import time

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By


# class Webscrape:
#     def __init__(self):
#         chromeOptions = uc.ChromeOptions().add_argument('--headless')
#         self.driver = uc.Chrome(chromeOptions)
#
#     # login = LogIn()
#     # login.login()

def scrape():
    page = 13444

    chrome_options = uc.ChromeOptions().add_argument('--headless')
    driver = uc.Chrome(chrome_options)
    for i in reversed(range(100)):
        url: str = f'https://www.illinoislottery.com/dbg/results/luckydaylotto/draw/{page}'
        driver.get(url)
        day_of_week = get_day_of_week(driver)
        date = get_date(driver)
        time_of_day = get_time_of_day(driver)
        first, second, third, fourth, fifth = get_first(driver), get_second(driver), get_third(driver), get_fourth(
            driver), get_fifth(driver)

        print_stuff(date, day_of_week, time_of_day)
        print_balls(first, second, third, fourth, fifth)
        page = page - 1
        time.sleep(random.randint(2, 6))


def get_date(driver):
    date = driver.find_element(By.XPATH,
                               '//*[@id="il-web-app"]/div[2]/div[2]/div/section/div/time/span[2]')
    return date


def get_day_of_week(driver):
    day_of_week = driver.find_element(By.XPATH, '//*[@id="il-web-app"]/div[2]/div[2]/div/section/div/time/span[4]')
    return day_of_week


def get_time_of_day(driver):
    time_of_day = driver.find_element(By.CSS_SELECTOR,
                                      '#il-web-app > div.book-container.book-container--luckydaylotto > '
                                      'div.exc-container.exc-container__body.exc-container--with-bottom-margin.book'
                                      '-container__content > div > section > div > time > '
                                      'span.dbg-result-details__draw-phase')
    return time_of_day


def get_first(driver):
    first = driver.find_element(By.ID, "result-line-primary-0-selected")
    return first


def get_second(driver):
    second = driver.find_element(By.ID, 'result-line-primary-1-selected')
    return second


def get_third(driver):
    third = driver.find_element(By.ID, 'result-line-primary-2-selected')
    return third


def get_fourth(driver):
    fourth = driver.find_element(By.ID, "result-line-primary-3-selected")
    return fourth


def get_fifth(driver):
    fifth = driver.find_element(By.ID, "result-line-primary-4-selected")
    return fifth


def print_stuff(date, day_of_week, time_of_day):
    print("Day of the week: ", day_of_week.text)
    print("Date: ", date.text)
    print("Time of day: ", time_of_day.text)


def print_balls(first, second, third, fourth, fifth):
    print("First: ", first.text)
    print("Second: ", second.text)
    print("Third: ", third.text)
    print("Fourth: ", fourth.text)
    print("Fifth: ", fifth.text)


scrape()
