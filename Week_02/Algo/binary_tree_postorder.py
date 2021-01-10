def postorderTraversal(self, root: TreeNode) -> List[int]:
        # res = []
        # def postOrder(root):
        #     if not root:
        #         return False
        #     postOrder(root.left)
        #     postOrder(root.right)
        #     res.append(root.val)
        # postOrder(root)
        # return res
        cur,stack,res = root,[],[]

        while cur or stack:
            while cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.right
            temp = stack.pop()
            cur = temp.left
        
        return res[::-1] 