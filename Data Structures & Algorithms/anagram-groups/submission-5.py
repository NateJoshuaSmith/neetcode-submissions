class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = defaultdict(list)

        for string in strs:
            #create a count list to represent 26 letters in the alphabet
            count = [0] * 26
            for c in string:
                #increment index that corresponds to that letters
                #ASCII value
                count[ord(c) - ord('a')] += 1
            #use that count array as a key for strings with the same 
            #number of letters
            groups[tuple(count)].append(string)
        #return a list of the list of strings
        return list(groups.values())

        