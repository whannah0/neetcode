class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointer
        max = 0
        #pointers
        left = 0
        right = len(heights)-1
        while right != left:
            minimum = min(heights[right], heights[left])
            area = (right - left) * minimum
            if area > max:
                max = area
            if minimum == heights[right]:
                right-=1
            else: 
                left +=1
        return max

        

        
        
        
        
        
        #brute force O(n^2)
        # max = 0
        # for i in range(len(heights)):
        #     for j in range(i+1, len(heights)):
        #         width = j-i
        #         if heights[i] < heights[j]:
        #             area = heights[i] * width
        #         else:
        #             area = heights[j] * width
                
        #         if area > max:
        #             max = area
        
        # return max
        