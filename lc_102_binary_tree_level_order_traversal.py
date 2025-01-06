# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dq = deque([root])
        res = []

        while len(dq) > 0:
            wrp = []
            for i in range(0, len(dq)):
                if len(dq) > 0:
                    cur = dq.popleft()

                    if cur:
                        wrp.append(cur.val)
                        dq.append(cur.left)
                        dq.append(cur.right)

            if len(wrp) > 0:
                res.append(wrp)
        return res

