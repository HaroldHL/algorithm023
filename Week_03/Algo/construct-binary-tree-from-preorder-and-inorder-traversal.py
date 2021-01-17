
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
            # 实际上inorder 和 postorder一定是同时为空的，因此你无论判断哪个都行
            if not preorder:
                return None
            # 前序遍历是根左右
            root = TreeNode(preorder[0])

            root_index = inorder.index(root.val)

            root.left = self.buildTree(preorder[1:root_index + 1], inorder[:root_index])
            root.right = self.buildTree(preorder[root_index + 1:], inorder[root_index+1:])

            return root

    # 时间复杂度：由于每次递归我们的inorder和preorder的总数都会减1，因此我们要递归N次，故时间复杂度为 O(N)，其中N为节点个数。
    # 空间复杂度：我们使用了递归，也就是借助了额外的栈空间来完成， 由于栈的深度为N，因此总的空间复杂度为 O(N)，其中N为节点个数。