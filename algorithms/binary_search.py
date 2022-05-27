# binary search in sorted array

def binary_search(arr, key):
    max = len(arr)
    mid = int(max / 2)
    
    if key > arr[mid]:
        return binary_search(arr[mid:], key)
    
    if key < arr[mid]:
        return binary_search(arr[:mid], key)
    
    return key

print(binary_search([1,2,3,4,5,6,7,8,9,10], 9))
