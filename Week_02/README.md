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
```

迭代的模板

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

