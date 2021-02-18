def maximalSquare(self, matrix: List[List[str]]) -> int:
    #若matrixmatrix为空，返回0
    if not matrix:
        return 0
    m=len(matrix)
    n=len(matrix[0])
    res=0
    dp=[[0]*(n+1) for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if matrix[i-1][j-1]=="1":
                dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
                res=max(dp[i][j],res)
    return res**2
#时间复杂度：O(m*n)O(m∗n)
#空间复杂度：O(m*n)O(m∗n)