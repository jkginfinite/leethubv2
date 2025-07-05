# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root):
        if not root:
            return []
        result = []
        stack = [root]

        while stack:
            node = stack.pop()

            if (not node.left) and (not node.right):
                result.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)   
        return result

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        L1 = self.helper(root1)
        L2 = self.helper(root2)
        return L1==L2


        