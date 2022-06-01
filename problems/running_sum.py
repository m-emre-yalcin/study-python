def running_sum(nums):
    return [sum(nums[:i + 1]) for i in range(len(nums))]

print(running_sum([1,1,1,1]))

# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1]