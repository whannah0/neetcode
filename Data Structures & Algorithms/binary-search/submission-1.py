class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        if n == 0:
            return -1

        if n == 1:
            if nums[0] == target:
                return 0
            else: 
                return -1

        #index
        l = 0
        r = n-1

        # // floor division
        

        while l <= r: 
            m = (l + r) // 2
            if target == nums[m]:
                return m
            elif target < nums[m]:
                r = m -1 
            else:
                l = m + 1
           
        
        return -1
        