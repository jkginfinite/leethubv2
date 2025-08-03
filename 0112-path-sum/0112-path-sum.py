# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        stack = [[root,root.val]]
        Sum = 0
        while stack:
            node,val = stack.pop()
            if node.left:
                stack.append([node.left,val+node.left.val])
            if node.right:
                stack.append([node.right,val+node.right.val])
            if not node.right and not node.left and val==targetSum:
                return True
        return False
        