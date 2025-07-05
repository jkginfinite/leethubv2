# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        stack = [root]
        result = set()

        while stack:
            node = stack.pop()
            result.add(node.val)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return len(result)==1
        