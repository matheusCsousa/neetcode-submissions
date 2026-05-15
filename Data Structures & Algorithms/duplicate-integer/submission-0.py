class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hMap = {}
        for i in nums:
            if i in hMap:
                hMap[i] += 1
            else:
                hMap[i] = 1
        
        for key in hMap:
            if hMap[key] > 1:
                return True
        return False