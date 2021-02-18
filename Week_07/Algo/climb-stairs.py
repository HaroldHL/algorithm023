class Solution:
    def climbStairs(self, n: int) -> int:
    # 直接递归
        # if n == 1:return 1
        # if n == 2:return 2
        # return self.climbStairs(n-1) + self.climbStairs(n-2)
    # DP
        # dp = {}
        # dp[1] = 1
        # dp[2] = 2
        # for i in range(3,n+1):
        #     dp[i] = dp[i-1] + dp[i-2]
        # return dp[n]

        if n==1 or n==2: return n
        a, b, temp = 1, 2, 0
        for i in range(3,n+1):
            temp = a + b
            a = b
            b = temp
        return temp