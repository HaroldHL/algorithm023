def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # base case
        if not root: return None
        if root == p or root == q: return root

        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if not left and not right: return # 1. p,q 都不在以root为根的树种
        if not left: return right # 3.只有一个存在于root中，函数返回改节点
        if not right: return left # 4.只有一个存在于root中，函数返回改节点
        return root # 2. if left and right:  p q 都在root为根的树中，left，right一定是p q
        # 时间复杂度：由于每次递归我们的inorder和preorder的总数都会减1，因此我们要递归N次，故时间复杂度为 O(N)，其中N为节点个数。
        # 空间复杂度：我们使用了递归，也就是借助了额外的栈空间来完成， 由于栈的深度为N，因此总的空间复杂度为 O(N)，其中N为节点个数。