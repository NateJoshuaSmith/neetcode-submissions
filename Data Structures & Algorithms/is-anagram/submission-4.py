class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Counter would have been better because it will automatically create the key
        # value pairs for me. I don't have to loop through and do it myself 
        freq_s = defaultdict(int)
        freq_t = defaultdict(int)

        if len(s) != len(t): return False

        for a, b in zip(s, t):
            freq_s[a] += 1
            freq_t[b] += 1

        return freq_s == freq_t

        