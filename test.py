import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.illinoislottery.com/{page}')
#print(response.text)
page = "results"

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.title)

blog_titles = soup.findAll('h2', attrs={"class":"blog-card__content-title"})
for title in blog_titles:
    print(title.text)
# Output:
# Prints all blog tiles on the page
#il-web-app > div.book-container.book-container--luckydaylotto > div.exc-container.exc-container--with-bottom-margin.book-container__content > div > section > div > div > div > div > div > div:nth-child(1)

#//*[@id="il-web-app"]/div[2]/div[2]/div/section/div/div/div/div/div/div[5]