# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root

        while curr:
            if curr.val < p.val and curr.val < q.val:
                curr = curr.right
            elif curr.val > p.val and curr.val > q.val:
                curr = curr.left
            else:
                return curr

    def lowestCommonAncestor2(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(root: TreeNode) -> TreeNode:
            if root.val < p.val and root.val < q.val:
                return dfs(root.right)
            elif root.val > p.val and root.val > q.val:
                return dfs(root.left)
            else:
                return root
        return dfs(root)
