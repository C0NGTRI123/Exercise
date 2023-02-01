def findNumbers():
    res = [i for i in range(1000, 3001) if all(int(b)%2==0 for b in str(i))]
    return res

print(findNumbers())