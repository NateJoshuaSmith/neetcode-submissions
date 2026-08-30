class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #I have an idea that you could do some sort of brute force solution where you start at index 1 and compare each element to see if its a match. The other idea that I had is to sort the strings. I assume there is a way to use hashing but I dont know what the key and value pairs would be. So now that I have had time to think about it I think what we want to do is we will sort each individual string in the list and create a key for that sorted value in our dictionary. We check each time has this key already been created and if it has and it matches we appened onto the list. ''.join(sorted(str))
        anagrams = defaultdict(list)
        for string in strs:
            key = ''.join(sorted(string))
            anagrams[key].append(string)
        return list(anagrams.values())




        