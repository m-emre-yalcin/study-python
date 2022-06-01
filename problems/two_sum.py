def two_sum(nums, target):
    for i, n in enumerate(nums):
        for i2, n2 in enumerate(nums[i:]):
            if i != i2 + i and n + n2 == target:
                return [i, i2 + i]

print(two_sum([3,2,4], 6))