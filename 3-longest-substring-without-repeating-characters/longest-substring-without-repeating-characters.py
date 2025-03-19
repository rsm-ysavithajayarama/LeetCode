class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        size = 0
        char = set()
        L = 0
        for R in range(len(s)):
            while s[R] in char:
                char.remove(s[L])
                L+=1
            char.add(s[R])
            size = max(size, R-L+1)
        return size
    
            