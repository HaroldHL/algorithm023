学习笔记



BFS 模板

```python
def BFS(graph, start, end): 
    visited = set()	
    queue = []
    queue.append([start])
    while queue:		
        node = queue.pop()		
        visited.add(node)
        
        process(node)		
        nodes = generate_related_nodes(node)		
        queue.push(nodes)	
        
        # other processing work	...
       
```

并查集模板

```python
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        
    def union(self, u, v):
        u_root = self.find(u)
        v_root = self.find(v)
        # 合并，连通分量数减少
        if u_root != v_root:
            self.parent[u_root] = v_root

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
```

红黑树的特性

stay tuned..

