class Solution:
    def climbStairs(self, n: int) -> int:
        # DP
        memo= [0] * (n+1) # ignore index 0

        #base case
        if n <= 1:
            return 1
        
        #ways(i) = ways (i-1) + ways(i-2)
        memo[0] = 1
        memo[1] = 1
        for i in range(2, n+1):
            memo[i] = memo[i-1] + memo[i-2]
        
        return memo[n]
        

        