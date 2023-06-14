import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Safari(executable_path='/nix/path/to/webdriver/executable')
driver.get('https://www.illinoislottery.com/dbg/results/luckydaylotto')
results = []
content = driver.page_source
soup = BeautifulSoup(content)
for element in soup.findAll(attrs={'class': 'title'}):
    name = element.find('a')
    results.append(name.text)