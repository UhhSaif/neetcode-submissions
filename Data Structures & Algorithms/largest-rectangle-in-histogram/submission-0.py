class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # pair (index, height)
        maxArea = 0 

        for i , h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                index, height = stack.pop()

                area = height * (i - index)
                maxArea = max(area, maxArea)

                start = index
            
            stack.append((start, h))

        for index, height in stack:
            area = height * (len(heights) - index)
            maxArea = max(maxArea, area)

        return maxArea