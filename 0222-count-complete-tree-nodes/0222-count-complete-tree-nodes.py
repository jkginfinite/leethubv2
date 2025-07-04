# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        result = 0
        if not root:
            return result
        
        stack = [root]

        while stack:
            node = stack.pop()
            result+=1

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result

        