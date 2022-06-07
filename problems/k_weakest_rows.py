def k_weakest_rows(mat, k):
    return list(map(lambda arr: arr[0] ,sorted([[i, mat[i].count(1)] for i in range(len(mat))], key=lambda arr: arr[1])))[:k]

print(k_weakest_rows(
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]],
 4))