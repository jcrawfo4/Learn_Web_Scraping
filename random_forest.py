# Data Processing
import sqlite3
import time

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier


class RandomForestClass:

    def __init__(self):
        self.con = sqlite3.connect('/Users/jacobcrawford/PycharmProjects/Learn_Web_Scraping/lotto_numbers')
        self.sql_query = pd.read_sql('select date, first, second, third, fourth, fifth from lotto_numbers', self.con)

        self.df = pd.DataFrame(self.sql_query, columns=['first', 'second', 'third', 'fourth', 'fifth'])
        self.con.close()

    def print_last_draw(self):
        last_draw = self.df.tail(1)
        return last_draw

    def predict_fifth(self):
        fifth = self.df['fifth']
        X_5 = self.df[['first', 'second', 'third', 'fourth']]

        rf_classifier = RandomForestClassifier(n_estimators=1000, random_state=42)
        rf_classifier.fit(X_5.values, fifth)
        input_to_guess = [1, 14, 23, 32]
        result = rf_classifier.predict(np.array(input_to_guess).reshape((1, -1)))[0]
        time.sleep(9)
        return result

    def predict_fourth(self):
        X_4 = self.df[['first', 'second', 'third', 'fifth']]
        fourth = self.df['fourth']

        rf_classifier = RandomForestClassifier(n_estimators=1000, random_state=42)
        rf_classifier.fit(X_4.values, fourth)
        input_to_guess = [6, 14, 23, 40]
        result = rf_classifier.predict(np.array(input_to_guess).reshape((1, -1)))[0]
        time.sleep(9)
        return result

    def predict_third(self):
        X_3 = self.df[['first', 'second', 'fourth', 'fifth']]
        third = self.df['third']

        rf_classifier = RandomForestClassifier(n_estimators=1000, random_state=42)
        rf_classifier.fit(X_3.values, third)
        input_to_guess = [6, 14, 32, 40]
        result = rf_classifier.predict(np.array(input_to_guess).reshape((1, -1)))[0]
        time.sleep(9)
        return result

    def predict_second(self):
        X_2 = self.df[['first', 'third', 'fourth', 'fifth']]
        second = self.df['second']

        rf_classifier = RandomForestClassifier(n_estimators=1000, random_state=42)
        rf_classifier.fit(X_2.values, second)
        input_to_guess = [6, 23, 32, 40]
        result = rf_classifier.predict(np.array(input_to_guess).reshape((1, -1)))[0]
        time.sleep(9)
        return result

    def predict_first(self):
        X_1 = self.df[['second', 'third', 'fourth', 'fifth']]
        first = self.df['first']

        rf_classifier = RandomForestClassifier(n_estimators=1000, random_state=42)
        rf_classifier.fit(X_1.values, first)
        input_to_guess = [14, 23, 32, 40]
        result = rf_classifier.predict(np.array(input_to_guess).reshape((1, -1)))[0]
        time.sleep(9)
        return result


def main():
    random_forest_class = RandomForestClass()
    print("Last draw: " + str(random_forest_class.print_last_draw()))
    result_5 = random_forest_class.predict_fifth()
    result_4 = random_forest_class.predict_fourth()
    result_3 = random_forest_class.predict_third()
    result_2 = random_forest_class.predict_second()
    result_1 = random_forest_class.predict_first()

    print(result_1, result_2, result_3, result_4, result_5)


if __name__ == '__main__':
    main()
