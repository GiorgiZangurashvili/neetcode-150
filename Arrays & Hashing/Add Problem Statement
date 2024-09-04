# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Constraints:
# s and t consist of lowercase English letters.

# Time Complexity: O(N + M)
# Space Complexity: O(1) (Since s and t only contain lowercase letters, maximum length of each hashmap will be 26)

class Solution:
    def getFreq(self, s: str) -> Dict[str, int]:
        res = {}

        for c in s:
            res[c] = res.get(c, 0) + 1
        
        return res

    def isAnagram(self, s: str, t: str) -> bool:
        return self.getFreq(s) == self.getFreq(t)
