from typing import List


def countPositiveNegativeNumber(data1: List):
    count_pos = 0
    count_neg = 0
    for data in data1:
        if data > 0:
            count_pos += 1
        else:
            count_neg += 1
    return count_pos, count_neg


data1 = [-10, -21, -4, -45, -66, 93, 11, -4, -6, 12, 11, 4]
print(countPositiveNegativeNumber(data1))
