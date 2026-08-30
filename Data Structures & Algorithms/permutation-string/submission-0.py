class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        matches = 0
        count1 = Counter(s1)
        count2 = Counter(s2[:len(s1)])
        
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if count1[c] == count2[c]:
                matches+=1
        
        l = 0
        for r in range(len(s1), len(s2)):

            if matches == 26:
                return True

            count2[s2[r]] += 1
            if count2[s2[r]] == count1[s2[r]]:
                matches += 1
            elif count2[s2[r]] - 1 == count1[s2[r]]:
                matches -= 1
            
            count2[s2[l]] -= 1
            if count2[s2[l]] == count1[s2[l]]:
                matches += 1
            elif count2[s2[l]] + 1 == count1[s2[l]]:
                matches -= 1
            
            l += 1
        
        return matches == 26






        
        