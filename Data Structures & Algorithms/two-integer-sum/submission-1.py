class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mHash = {}
        for i, n in enumerate(nums):
            if target-n in mHash:
                return [mHash[target-n], i]
            mHash[n] = i 
        return []
