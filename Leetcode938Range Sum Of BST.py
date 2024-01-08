# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def function(node):
            nonlocal res
            if node:
                if node.val in range(low, high + 1):
                    res += node.val
                if node.val > low:
                    function(node.left)
                if node.val < high:
                    function(node.right)

        res = 0
        function(root)
        return res