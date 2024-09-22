# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
# Each product is guaranteed to fit in a 32-bit integer.
# Follow-up: Could you solve it in O(n) time without using the division operation?

# Constraints:
# 2 <= nums.length <= 1000
# -20 <= nums[i] <= 20

# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(1, len(res)):
            res[i] = prefix * nums[i - 1]
            prefix = res[i]

        postfix = nums[-1]
        for i in range(len(res) - 2, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res
