data4 = [1,2,3]
for i in range(len(data4)):
    for j in range(len(data4)):
        for k in range(len(data4)):
            if(i!=j and j!=k and k!=i):
                print(data4[i], data4[j], data4[k])