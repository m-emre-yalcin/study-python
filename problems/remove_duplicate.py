def remove_duplicates(nums):
    i = 0
    while i < len(nums):
        if i and nums[i] == nums[i - 1]:
            nums.pop(i)
            i=-1
        i+=1
    return nums

print(remove_duplicates([1,2,2,3,4,4,6]))