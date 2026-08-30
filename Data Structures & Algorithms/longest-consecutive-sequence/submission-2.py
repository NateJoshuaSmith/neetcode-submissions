class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        sorted_nums = set(nums)
        longest = 0

        for num in sorted_nums:
            if num - 1 not in sorted_nums:
                length = 1
                current = num
                while current + 1 in sorted_nums:
                    current += 1
                    length += 1                
                longest = max(length, longest)
        
        return longest