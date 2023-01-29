from typing import List

def maxAdj(data3: List):
    res = []
    print(len(data3))
    for i in range(1, len(data3)):
        r = max(data3[i], data3[i-1])
        res.append(r)
    return res

data3 = [4, 5, 6, 7, 3, 9, 11, 2, 10]
print(maxAdj(data3))