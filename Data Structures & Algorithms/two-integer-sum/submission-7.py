class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums contains an array of integers
        # target is the sum of the two indicies values we are looking for
        # return i and j when you find nums[i] + nums[j] == target and
        # i != j

        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return[seen[complement], i]
            else:
                seen[num] = i
        return []





        