class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])

        dp = [0] * (n+1)
        dp[0] = 0 #ignore index 0
        dp[1] = nums[0]
        dp[2] = nums[1]

        maxSoFar=0
        for i in range(3, n+1):
            for j in range(0, i-1):
                if dp[j] > maxSoFar:
                    maxSoFar = dp[j]
            dp[i] = maxSoFar + nums[i-1]
        
        return max(dp[n-1], dp[n])