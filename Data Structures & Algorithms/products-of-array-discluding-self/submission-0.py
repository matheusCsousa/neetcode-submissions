class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prod = 1
        for i, n in enumerate(nums):
            for j, k in enumerate(nums):
                if i == j: continue
                prod *= nums[j]
            res.append(prod)
            prod = 1
        return res 
                