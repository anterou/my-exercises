class Solution:
    def twoSum(self, nums, target):
        var = {}
        for i, value in enumerate(nums):
            remaining = target - nums[i]
            if remaining in var:
                return (i, var[remaining])
            else:
                var[value] = i