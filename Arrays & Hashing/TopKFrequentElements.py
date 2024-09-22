# Given an integer array nums and an integer k, return the k most frequent elements within the array.
# The test cases are generated such that the answer is always unique.
# You may return the output in any order.

# Constraints:
# 1 <= nums.length <= 10^4.
# -1000 <= nums[i] <= 1000
# 1 <= k <= number of distinct elements in nums.

# Time Complexity: O(N)
# Space Complexity: O(N)


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}

        for num in nums:
            freqMap[num] = 1 + freqMap.get(num, 0)
        
        topKArr = [[] for _ in range(len(nums) + 1)]

        for key, val in freqMap.items():
            topKArr[val].append(key)
        
        res = []
        for i in range(len(topKArr) - 1, -1, -1):
            res.extend(topKArr[i])
        
        return res[0:k]
        
