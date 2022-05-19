def selection_sort(arr):
    for i, n in enumerate(arr):
        for j, n in enumerate(arr[i:]):
            if arr[i] > arr[i + j]:
                tmp = arr[i]
                arr[i] = arr[i + j]
                arr[i + j] = tmp
    return arr

print(selection_sort([4,6,8,43,6,8,34,9,12]))