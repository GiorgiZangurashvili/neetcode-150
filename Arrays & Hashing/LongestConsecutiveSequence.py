# Given an array of integers nums, return the length of the longest consecutive sequence of elements.
# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.
# You must write an algorithm that runs in O(n) time.

# Constraints:
# 0 <= nums.length <= 1000
# -10^9 <= nums[i] <= 10^9

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)

        maxSize = 0
        for i, num in enumerate(nums):
            if (num - 1) not in hashset:
                size = 1
                currNum = num + 1
                while currNum in hashset:
                    currNum += 1
                    size += 1
                maxSize = max(maxSize, size)
        
        return maxSize
