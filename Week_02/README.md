学习笔记

4 步法
* clarification
* possible solution --> optimal(time & space)
* code
* test


二叉树
如果你按照 根节点 -> 左孩子 -> 右孩子 的方式遍历，即「先序遍历」
左孩子 -> 根节点 -> 右孩子 的方式遍历，即「中序序遍历」
左孩子 -> 右孩子 -> 根节点 的方式遍历，即「后序序遍历」

三者都有一个固定的模板，只需将递归函数里的 res.append(root.val) 放在不同位置即可，然后调用这个递归函数就可以了，代码完全一样。

```python
def dfs(root):
  res = []
  if not root:
    return
  
  res.append(root.val) #前序
  dfs(root.left)
  dfs(root.right)

dfs(root)
return res

def dfs(root):
  res = []
  if not root:
    return
  
  dfs(root.left)
	res.append(root.val) #中序
  dfs(root.right)

dfs(root)
return res

dfs(root)
return res

def dfs(root):
  res = []
  if not root:
    return
  
  dfs(root.left)
  dfs(root.right)
  res.append(root.val) #后序

dfs(root)
return res
```

迭代的解法

a:

* 初始化栈，讲根节点入栈
* 栈不为空的时候：
  * 弹出栈顶Node，并且将值添加到结果中
  * 如果node的右子树不为空，右子树先入栈(这边是前序，因为栈的特性是先进后出)
  * 如果node的左子树不为空，左子树入栈 

```python
def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:return []
        stack, res = [root],[]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return res
```

*模板解法*

* 先将根节点 `cur` 和所有的左孩子入栈并加入结果中，直至 `cur` 为空，用一个 `while` 循环实现
* 每弹出一个栈顶元素temp 就达到它的右孩子，再将整个节点当做`cur`重新按上面的步骤来一遍，直至栈为空。需要一个while循环

```python
def preorderTraversal(self, root: TreeNode) -> List[int]:
  	if not root:return []
        
        cur,stack,res = root,[],[]
        while cur or stack:
            while cur: # 根节点和左孩子入栈
                res.append(cur.val)
                stack.append(cur)
                cur = cur.left
            temp = stack.pop() # 每次弹出一个元素，就达到右孩子
            cur = temp.right
        return res
      
```

```python
#中序

def inorderTraversal(self, root: TreeNode) -> List[int]:
  	if not root: return
    
    cur,stack,res = root,[],[]
    
    while cur or stack:
      while cur: 
        stack.append(cur)
        cur = cur.left
      temp = stack.pop()
      res.append(temp.val) # 出栈时加入结果
      cur = temp.right
    return res
```
点 `cur` 先到达最右端的叶子节点并将路径上的节点入栈；

然后每次从栈中弹出一个元素后，`cur` 到达它的左孩子，并将左孩子看作 `cur` 继续执行上面的步骤。

最后将结果反向输出即可

```python

 def postorderTraversal(self, root: TreeNode) -> List[int]:
        cur,stack,res = root,[],[]

        while cur or stack:
            while cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.right
            temp = stack.pop()
            cur = temp.left
        
        return res[::-1] 
```





append() VS extend() in Python ?

**[extend()](https://www.geeksforgeeks.org/list-methods-python/):** Iterates over its argument and adding each element to the list and extending the list. The length of the list increases by number of elements in it’s argument.

```python

my_list = ['geeks', 'for'] 
another_list = [6, 0, 4, 1] 
my_list.extend(another_list) 
print my_list  #['geeks', 'for', 6, 0, 4, 1]

my_list = ['geeks', 'for', 6, 0, 4, 1] 
my_list.extend('geeks') 
print my_list #['geeks', 'for', 6, 0, 4, 1, 'g', 'e', 'e', 'k', 's']

Time Complexity:
Append has constant time complexity i.e.,O(1).
Extend has time complexity of O(k). Where k is the length of list which need to be added.
```

python获取value的方法：

```
dict.values()
```

