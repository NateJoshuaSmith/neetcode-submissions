class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        length = 0
        duplicate_char = set()
        l, r = 0, 1

        for r in range(len(s)):
            while s[r] in duplicate_char:
                duplicate_char.remove(s[l])
                l += 1
            duplicate_char.add(s[r])

            length = max(length, r - l + 1)     
        return length  
