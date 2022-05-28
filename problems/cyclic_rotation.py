def cyclic_rotation(A, K):
    i = 0
    while i < K:
        last = A.pop()
        A.insert(0, last)
        i+=1
    return A

print(cyclic_rotation([1,2,3], 2))