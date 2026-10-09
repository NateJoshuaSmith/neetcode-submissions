class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #the key would be the number and the value would be the index
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            else:
                seen[num] = i
        return []
        