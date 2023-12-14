import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

driver = uc.Chrome(use_subprocess=True)


# driver.get('https://www.illinoislottery.com/dbg/results/luckydaylotto/draw/9999')


# driver.find_element(By.XPATH, '/html/body/main/div[2]/div[2]/div/section/div/div/div/div/div[1]/div/div[2]')


def get_day_of_week(d):
    day_of_week = d.find_element(By.XPATH, '//*[@id="il-web-app"]/div[2]/div[2]/div/section/div/time/span[1]')
    day_of_week = str(day_of_week.text.strip())[0:-1]
    return day_of_week.strip()


def get_time_of_day(d):
    time_of_day = d.find_element(By.XPATH,
                                 '//*[@id="il-web-app"]/div[2]/div[2]/div/section/div/time/span[4]')
    return str(time_of_day.text.strip()).strip()


for i in range(9990, 9999):
    url = f'https://www.illinoislottery.com/dbg/results/luckydaylotto/draw/{i}'
    driver.get(url)
    week_day = get_day_of_week(driver)
    print(week_day)
    time_of_day = get_time_of_day(driver)
    print(time_of_day)

driver.quit()
