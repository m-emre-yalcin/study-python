def selection_sort(array):
    size = len(array)

    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
         
        # put min at the correct position
        array[step], array[min_idx] = array[min_idx], array[step]
    return array

# time complexity
# best: O(n2)
# average: O(n2)
# worst: O(n2)

print(selection_sort([4,6,8,43,6,8,34,9,12]))