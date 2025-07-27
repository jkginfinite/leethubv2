# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        stack = [root]
        values = []

        while stack:
            node = stack.pop()
            values.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        stack2 = [root]
        while stack2:
            node = stack2.pop()
            node.val+=sum([j for j in values if j>node.val])
            if node.left:
                stack2.append(node.left)
            if node.right:
                stack2.append(node.right)
        return root