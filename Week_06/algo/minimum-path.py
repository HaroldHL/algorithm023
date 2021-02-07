
def minPathSum(self, grid: List[List[int]]) -> int:
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # 起点
            if i == j == 0: continue
            # 上边界
            elif i == 0: grid[i][j] = grid[i][j]+ grid[i][j-1]
            # 左边界
            elif j == 0: grid[i][j] = grid[i][j]+ grid[i-1][j]
            else: grid[i][j] = min(grid[i-1][j],grid[i][j-1]) + grid[i][j]
    return grid[-1][-1]