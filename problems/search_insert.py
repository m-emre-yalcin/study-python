# https://leetcode.com/problems/search-insert-position/
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

def search_insert(arr, target):
    def search_for_target(arr, ind=0):
        max = len(arr)
        mid = max // 2

        if target == arr[mid]:
            ind = ind + mid
            return ind
        
        # edge case
        elif mid == 0:
            if target > arr[mid]: return ind + 1 # end
            else: return ind # start

        if target > arr[mid]:
            ind = ind + mid
            return search_for_target(arr[mid:], ind)

        if target < arr[mid]:
            return search_for_target(arr[:mid], ind)

    return search_for_target(arr)

print(search_insert([1,3,5,6,7,9,10],7))