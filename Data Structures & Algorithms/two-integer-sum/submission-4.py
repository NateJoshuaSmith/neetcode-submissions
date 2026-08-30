class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        prev_num = {}

        for i, num in enumerate(nums):
            difference = target - num
            if difference in prev_num:
                return [prev_num[difference], i]
            else:
                prev_num[num] = i
        return []