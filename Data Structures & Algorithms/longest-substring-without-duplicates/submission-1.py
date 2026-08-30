class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        result = 0
        duplicate_char = set()
        l = 0
        for r in range(len(s)):
            while s[r] in duplicate_char:
                duplicate_char.remove(s[l])
                l += 1
            duplicate_char.add(s[r])
            result = max(result, r - l + 1)
        return result



        




        