class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #List Comprehension:

        return [num for num, count in Counter(nums).most_common(k)]






        