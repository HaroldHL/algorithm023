class UnionFind:
    """并查集
    """
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        # 初始连通分量数为 n 个
        self.count = n
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, u, v):
        u_root = self.find(u)
        v_root = self.find(v)
        # 合并，连通分量数减少
        if u_root != v_root:
            self.parent[u_root] = v_root
            self.count -= 1
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        #DFS 遍历所有城市，对于每个城市，如果该城市尚未被访问过，则从该城市开始深度优先搜索，通过矩阵 isConnected 得到与该城市直接相连的城市有哪些，这些城市和该城市属于同一个连通分量，然后对这些城市继续深度优先搜索，直到同一个连通分量的所有城市都被访问到，即可得到一个省份。遍历完全部城市以后，即可得到连通分量的总数，即省份的总数
        # def dfs(i):
        #     for j in range(N):
        #         if isConnected[i][j] and j not in visited:
        #             visited.add(j)
        #             dfs(j)
        # N = len(isConnected)
        # count = 0
        # visited = set()

        # for i in range(N):
        #     if  i not in visited:
        #         count += 1
        #         visited.add(i)
        #         dfs(i)
        
        # return count

        #Union-Find
        n = len(isConnected)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    # 有相连关系，则进行合并
                    uf.union(i, j)
        return uf.count

       