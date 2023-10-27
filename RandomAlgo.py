import random as r


class RandomAlgo:
    weights = []

    def __init__(self):
        self.result = self.side_decider
        print(self.result)

    @property
    def side_decider(self):
        side = r.randint(0, 3)
        if side == 0:
            print("side", side)
            left = self.make_combo_from_first
            return left
        elif side == 1:
            print("side", side)
            right = self.make_combo_from_last
            return right
        elif side == 2:
            print("side", side)
            middle = self.make_combo_from_third
            return middle
        else:
            print("side", side)
            median = self.make_combo_from_median
            return median

    @property
    def make_combo_from_first(self):
        first = r.randint(1, 38)
        second = r.randint(first + 1, 42)
        third = r.randint(second + 1, 43)
        fourth = r.randint(third + 1, 44)
        fifth = r.randint(fourth + 1, 45)
        return [first, second, third, fourth, fifth]

    @property
    def make_combo_from_last(self):
        fifth = r.randint(9, 45)
        fourth = r.randint(5, fifth - 1)  # fourth has to be smaller than fifth
        third = r.randint(3, fourth - 1)
        second = r.randint(2, third - 1)
        first = r.randint(1, second - 1)
        return [first, second, third, fourth, fifth]

    @property
    def make_combo_from_third(self):
        third = r.randint(3, 43)
        fourth = r.randint(third + 1, 44)
        second = r.randint(2, third - 1)
        fifth = r.randint(fourth + 1, 45)
        first = r.randint(1, second - 1)
        return [first, second, third, fourth, fifth]

    @property
    def make_combo_from_median(self):
        medians = [6, 14, 23, 31, 40]
        median = r.choice(medians)
        if median == 6:
            first = median
            second = r.randint(first + 1, 42)
            third = r.randint(second + 1, 43)
            fourth = r.randint(third + 1, 44)
            fifth = r.randint(fourth + 1, 45)
        elif median == 14:
            first = r.randint(1, median - 1)
            second = median
            third = r.randint(median + 1, 43)
            fourth = r.randint(third + 1, 44)
            fifth = r.randint(fourth + 1, 45)
        elif median == 23:
            third = median
            second = r.randint(2, third - 1)
            first = r.randint(1, second - 1)
            fourth = r.randint(third + 1, 44)
            fifth = r.randint(fourth + 1, 45)
        elif median == 31:
            fourth = median
            third = r.randint(3, fourth - 1)
            fifth = r.randint(fourth + 1, 45)
            second = r.randint(2, third - 1)
            first = r.randint(1, second - 1)
        else:
            fifth = median
            fourth = r.randint(5, fifth - 1)
            third = r.randint(3, fourth - 1)
            second = r.randint(2, third - 1)
            first = r.randint(1, second - 1)
        return [first, second, third, fourth, fifth]


ra = RandomAlgo()
