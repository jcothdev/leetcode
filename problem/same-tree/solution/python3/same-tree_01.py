# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        isSame = False
        if p.val == q.val and (p.left and q.left):
            if p.left.val == q.left.val:
                print("QQ")
            if (p.left and q.left) and (p.right.val == q.right.val):
                print("QQQ")
                isSame = True
        return isSame
