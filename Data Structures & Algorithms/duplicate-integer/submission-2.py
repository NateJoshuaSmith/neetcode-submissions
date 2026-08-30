class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        sorted_nums = sorted(nums)

        for curr, nxt in zip(sorted_nums, sorted_nums[1:]):
            if curr == nxt:
                return True
        return False

