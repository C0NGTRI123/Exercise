from typing import List


def ex2(data2:List, K:int):

    for i in data2:
        freq = data2.count(i)

        if freq>K and i not in res:
            res.append(i)
    return res

data2 = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
K = 3
print(ex2(data2, K))


