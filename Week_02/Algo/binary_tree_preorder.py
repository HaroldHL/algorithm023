 def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 递归的方式类似模板 前序是根-左-右
        def preorderTraversal(self, root: TreeNode) -> List[int]:
            res = []
            def dfs(root):
                if not root:
                    return False
                res.append(root.val)
                dfs(root.left)
                dfs(root.right)
            dfs(root)
            return res  
        #iterative template solution
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

