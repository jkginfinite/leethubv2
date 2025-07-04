# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        Sum = 0
        if not root:
            return Sum

        queue = [[root,None]]
        while queue:
            node, LR = queue.pop(0)
            if node.left:
                v = [node.left,'left']
                queue.append(v)
            if node.right:
                v = [node.right,'right']
                queue.append(v)
            if (not node.right) and (not node.left) and (LR=='left'):
                Sum+=node.val
        return Sum
        