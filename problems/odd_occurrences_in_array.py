def odd_occurrences_in_array(A):
    A.sort()
    i = 0
    N = len(A)

    while i < N:
        if A[i] == A[-1]:
            return A[i]
        elif A[i] == A[i+1]:
            i+=2 # 2 step ahead
        else:
            return A[i]

print(odd_occurrences_in_array([42]))