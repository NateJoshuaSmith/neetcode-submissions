class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # There are two approaches that come to mind first one is sorting, but that would be O(nlongn)

        compareS = sorted(s)
        compareT = sorted(t)

        return compareS == compareT