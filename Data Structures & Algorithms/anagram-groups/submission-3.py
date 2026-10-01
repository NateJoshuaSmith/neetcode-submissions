class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # you could sort the strings in the list and compare them
        # Constraints: 1 to 10000 words, each word is 0 to 100 characters
        # all lowercase characters
        
        groups = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            groups[tuple(count)].append(s)
        return list(groups.values())
        
        