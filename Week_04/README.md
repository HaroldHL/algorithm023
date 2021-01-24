学习笔记

DFS的模板

```python
# 递归的写法
visited = set() 
def dfs(node, visited):    
  if node in visited: # terminator    	
    # already visited     	
    return 	
  
  visited.add(node) 	
  # process current node here. 	
  ...	
  for next_node in node.children(): 		
    if next_node not in visited: 			
      dfs(next_node, visited)
      
      
# 非递归的写法
def DFS(self, tree): 	
  if tree.root is None: 		
    return [] 	
  visited, stack = [], [tree.root]	
  
  while stack: 		
    node = stack.pop() 		
    visited.add(node)		
    
    process (node) 		
    nodes = generate_related_nodes(node) 		
    stack.push(nodes) 	
    # other processing work 	
    ...
```

BFS的模板

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
    
  # other processing work 	
  ...
```



二分查找的模板

```python
left, right = 0,len(nums)-1
while(...):
  mid = left + (right-left)/2
  if nums[mid] == target:
    # find the target
    break or return result
  elif nums[mid]< target:
    left =...
  elif nums[mid]> target:
    right = ...
    
return ...
  
  
  
```

* 尽量不要出现else，而是把所有的情况用else if写清楚，这样可以展示所有的细节；

* mid = (left + right) / 2 在强类型的语言内可能导致**数字越界**，那么可以采用

mid = left + (right - left) / 2

* 三个前提条件
  * 1.目标函数单调性(单调递增或者递减)
  * 2.存在上下界(bounded)
  * 3.能够通过索引访问(index accessible)

* 寻找一个半有序数组 [4, 5, 6, 7, 0, 1, 2] 中间无序的地方 test.py

  ```python
  
  while left <= right: 
              mid = left + (right - left) // 2
              if nums[mid] > nums[mid+1]: return nums[mid+1]
              if nums[mid] < nums[mid-1]: return nums[mid]
              if nums[mid] < nums[0]: right = mid - 1
              if nums[mid] > nums[0]: left = mid + 1
  ```

  

  

