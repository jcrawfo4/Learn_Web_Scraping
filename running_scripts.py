import numpy as np
import pandas as pd
import matplotlib as plt

winners = pd.to_csv('/Users/cdmstudent/Documents/PyCharmProjects/Learn_Web_Scraping/lotto_results', sep=',')

winners.describe(include = 'all')