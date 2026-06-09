class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #brute force
        max = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                width = j-i
                if heights[i] < heights[j]:
                    area = heights[i] * width
                else:
                    area = heights[j] * width
                
                if area > max:
                    max = area
        
        return max
        