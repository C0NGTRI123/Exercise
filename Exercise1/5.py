def add_matrices(mat1,mat2):
    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[i])):
            row.append(mat1[i][j])
        for j in range(len(mat2[i])):
            row.append(mat2[i][j])
        result.append(row)
    return result

test_list1 = [[4, 3, 5], [1, 2, 3], [3, 7, 4]]
test_list2 = [[1], [9], [8]]
print(add_matrices(test_list1, test_list2))