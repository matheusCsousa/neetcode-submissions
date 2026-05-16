class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        triplets = []
        for i in range(len(nums)):
            current = nums[i]
            if i > 0 and current == nums[i-1]:
                continue

            l, r = i+1, len(nums)-1
            while l < r:
                sum3 = current + nums[l] + nums[r] 
                if sum3 > 0:
                    r-=1
                elif sum3 < 0:
                    l+=1
                else:
                    triplets.append([nums[l], nums[i], nums[r]])
                    l+=1
                    while  l < r and nums[l]  == nums[l-1]:
                        l+=1
                    
        return triplets