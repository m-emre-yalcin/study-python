def insertion_sort(arr):
    for step in range(1, len(arr)):
        key = arr[step]
        j = step - 1

        while j >=0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = key
    return arr
# time complexity: O(n2)
# space complexity: O(1)

print(insertion_sort([4,7,6,3,3,10]))