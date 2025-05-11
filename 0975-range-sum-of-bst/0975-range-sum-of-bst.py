
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        values = []
        node = root
        stack = []
        while node or stack:
            #go as left as possible
            while node:
                stack.append(node)
                node = node.left
            #visit node
            node = stack.pop()
            values.append(node.val)
            #move to the right subtree
            node = node.right
        return sum([i for i in values if i in range(low,high+1)])

                
        