import urllib.request

import bs4
import pandas as pd
from random import randint # this random pause and restart of the loop below prevents me getting my ip banned.
from time import sleep

page = 2
results = []
big_arr = []
pd.DataFrame(results).to_csv("/lotto_results_trial.txt", index_label=None, columns=None, header=False)
url = 'https://www.illinoislottery.com/dbg/results/luckydaylotto'
url_contents = urllib.request.urlopen(url).read()
soup = bs4.BeautifulSoup(url_contents, features="lxml")
for j in range(1, 11):
    content = []
    for i in range(5):
        div = soup.find("div", {"data-test-id": f"ball-primary-{i}-{j}"}).contents[0].strip()
        content.append(str(div))
    results.append(content)

for page in range(2, 580):
    url = f'https://www.illinoislottery.com/dbg/results/luckydaylotto?page={page}'
    url_contents = urllib.request.urlopen(url).read()
    soup = bs4.BeautifulSoup(url_contents, features="lxml")
    for j in range(1, 11):
        content = []
        sleep(randint(2,6))
        for i in range(5):
            div = soup.find("div", {"data-test-id": f"ball-primary-{i}-{j}"}).contents[0].strip()
            content.append(str(div))
        results.append(content)
print(results[-1])
# np.savetxt("lotto_results", results, delimiter=",", header="first, second, third, fourth, fifth", fmt='% s', comments='')
pd.DataFrame(results).to_csv("/lotto_results_trial.txt", index_label=None, columns=None, header=False, index=None)

