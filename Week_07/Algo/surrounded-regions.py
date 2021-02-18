class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #Step 1:边界上的O找到变成A
        #Step 2:遍历整个board,把O变成X,A为成0
        # if not board or not board[0]:
        #     return
        # row = len(board)
        # col = len(board[0])

        # def dfs(i, j):
        #     """
        #     深度优先算法，如果符合条件，替换为A并进一步测试，否则停止
        #     """
        #     if i < 0 or j < 0 or i >= row or j >= col or board[i][j] != 'O':
        #         return
        #     board[i][j] = 'A'
            
        #     dfs(i - 1, j)
        #     dfs(i + 1, j)
        #     dfs(i, j - 1)
        #     dfs(i, j + 1)
        
        # # 从外围开始
        # for i in range(row):
        #     dfs(i, 0)
        #     dfs(i, col-1)
        
        # for j in range(col):
        #     dfs(0, j)
        #     dfs(row-1, j)
        
        # # 最后完成替换
        # for i in range(row):
        #     for j in range(col):
        #         if board[i][j] == 'O':
        #             board[i][j] = 'X'
        #         elif board[i][j] == 'A':
        #             board[i][j] = 'O'

        


        
