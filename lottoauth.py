import random

import undetected_chromedriver as uc
import time
from selenium.webdriver.common.by import By


class LottoAuth:
    def __init__(self):
        self.username = "CheekTeam@yahoo.com"
        self.password = "CheekTeam1!"
        self.uname = None
        self.pword = None
        self.chromeOptions = uc.ChromeOptions().add_argument('--headless')
        self.driver = uc.Chrome()

    def login(self):
        self.driver.get('https://www.illinoislottery.com/account/login')
        self.uname = self.driver.find_element(By.ID, "userName")
        self.uname.send_keys(self.username)
        self.pword = self.driver.find_element(By.ID, "password")
        self.pword.send_keys(self.password)
        self.driver.find_element(By.ID, "login-button").click()
        randint = random.randint(29, 88)
        time.sleep(randint)

    def logout(self) -> None:
        self.driver.get('https://www.illinoislottery.com/account/profile')
        self.driver.find_element(By.XPATH, '//*[@id="il-web-app"]/div[4]/div/section/div/div[1]/div/section[7]/form/button').click()
        self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    login = LottoAuth()
    login.login()
    login.logout()
