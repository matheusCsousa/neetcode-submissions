class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        search = set(nums)
        longest = 0

        for num in search:
            if num-1 not in search:
                length = 1
                while (num + length) in search:
                    length += 1
                longest = max(length, longest)
        return longest