def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# time complexity
# best: O(n)
# average: O(n2)
# worst: O(n2)

# space complexity
# O(1)

print(bubble_sort([2,6,8,9,11,3,7]))