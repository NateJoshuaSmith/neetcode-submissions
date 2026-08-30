class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        # a + b = target (subtract b -->) a = target - b
        for i, value in enumerate(nums):
            complement = target - value

            if complement in seen:
                return[seen[complement], i]

            seen[value] = i
        