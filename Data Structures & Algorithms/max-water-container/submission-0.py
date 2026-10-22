class Solution:
    def maxArea(self, heights: List[int]) -> int:
        total = 0
        l, r = 0, len(heights) - 1

        while l < r:
            width = r - l
            height = min(heights[r], heights[l])
            
            if width * height > total:
                total = width * height
            if heights[r] == height:
                r -= 1
            elif heights[l] == height: 
                l += 1
        return total

