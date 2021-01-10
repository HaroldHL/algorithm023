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

先将根节点 `cur` 和所有的左孩子入栈并加入结果中，直至 `cur` 为空，用一个 `while` 循环实现：

