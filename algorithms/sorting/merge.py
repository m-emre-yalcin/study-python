def sort(arr):
    # best case
    if len(arr) == 1:
        return arr

    midpoint = len(arr) // 2
    left = arr[:midpoint]
    right = arr[midpoint:]

    return merge(sort(left), sort(right))

def merge(left, right):
    res = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i = i + 1
        else:
            res.append(right[j])
            j = j + 1

    return res + left[i:] + right[j:]

# time complexity
# worst case: O(n logn) = linearithmic
# avarage case: O(n logn)

# space complexity: O(n) = linear

# merge sort requires additional memory space to store the auxiliary arrays.

print(sort([1,3,4,2]))