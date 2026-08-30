#my first thought is to have two loops and compare each index with every other element in the array until we find the target.
        #One key to keep in mind is when you see a problem like this try to isolate what you are looking for algerbraicly. i + j = target if we want to find the value of what i would be we solve that algerbraiclly. i = target - j
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i in range(len(nums)):
            if (target - nums[i]) in seen:
                return [seen[target - nums[i]], i]
            else:
                seen[nums[i]] = i


