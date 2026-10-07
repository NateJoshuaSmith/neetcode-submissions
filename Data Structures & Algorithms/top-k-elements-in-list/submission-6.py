class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #create a hash map (Counter) to store all of the numbers and their
        #frequencies
        count = Counter(nums)

        #we want to create the empty list of buckets to be the size
        #of the nums array + 1 
        buckets = [[] for _ in range(len(nums) + 1)]

        #our list is sorted by index from most frequent to least frequent
        #we want to loop backwards through buckets to get the top
        #frequent k
        for num, freq in count.items():
            buckets[freq].append(num)
        
        #We want to create an empty results list
        results = []
        #itterate through the buckets list backwards 
        for freq in range(len(buckets) - 1, 0, -1):
            #access the inner list of the buckets list
            for num in buckets[freq]:
                results.append(num)
                if len(results) == k:
                    return results
                #append the first numbers in the list
        return results









        
        