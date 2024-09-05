# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Constraints:
# 1 <= strs.length <= 1000.
# 0 <= strs[i].length <= 100
# strs[i] is made up of lowercase English letters.

# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for s in strs:
            arr = [0] * 26

            for c in s:
                arr[ord(c) - ord('a')] += 1
            
            hashmap[tuple(arr)].append(s)
        
        return hashmap.values()
