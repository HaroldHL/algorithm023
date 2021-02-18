class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
    # dfs的解法
    #     if not grid:return 0
    #     count = 0   
    #     for i in range(len(grid)):
    #         for j in range(len(grid[0])):
    #             if grid[i][j] == "1":
    #                 self.dfs(grid, i, j)
    #                 count += 1
    #     return count

    # def dfs(self, grid, i, j):
    #     if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
    #         return 
    #     grid[i][j] = '0'
    #     self.dfs(grid, i + 1, j)
    #     self.dfs(grid, i - 1, j)
    #     self.dfs(grid, i, j + 1)
    #     self.dfs(grid, i, j - 1)

    #Union-Find
        if len(grid) == 0: 
            return 0
        row = len(grid); col = len(grid[0])
        self.count = sum(grid[i][j]=='1' for i in range(row) for j in range(col))
        parent = [i for i in range(row*col)]
        
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        def union(u,v):
            u_root = find(u)
            v_root = find(v)
            if u_root != v_root:
                parent[u_root] = v_root
                self.count -=1
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '0':
                    continue
                index = i*col + j
                if j < col-1 and grid[i][j+1] == '1':
                    union(index, index+1)
                if i < row-1 and grid[i+1][j] == '1':
                    union(index, index+col)
        return self.count
