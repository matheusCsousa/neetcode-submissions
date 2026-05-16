class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest = 0

        l, r = 0, len(heights)-1
        while l < r:
            current = (r-l) * min(heights[l], heights[r])
            if current > largest:
                largest = current
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return largest