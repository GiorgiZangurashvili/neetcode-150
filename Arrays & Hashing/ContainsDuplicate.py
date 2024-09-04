# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        
        return False
