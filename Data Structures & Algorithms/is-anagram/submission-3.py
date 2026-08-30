class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        sorted_string1 = sorted(s)
        sorted_string2 = sorted(t)
        
        return sorted_string1 == sorted_string2
        