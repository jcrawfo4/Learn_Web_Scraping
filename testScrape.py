import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

driver = uc.Chrome(use_subprocess=True, headless=True)
driver.get('https://www.illinoislottery.com/dbg/results/luckydaylotto/draw/14325')


def get_day_of_week(driver):
    day_of_week = driver.find_element(By.XPATH, '//*[@id="il-web-app"]/div[2]/div[2]/div/section/div/time/span[1]')
    day_of_week = str(day_of_week.text.strip())[0:-1]
    return day_of_week.strip()


print(get_day_of_week(driver))
