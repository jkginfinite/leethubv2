# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flattenTree(self, node):
        #handle the node being null
        if not node:
            return None
        #for a lead node, return it as is
        if not node.left and not node.right:
            return node
        
        #recursively flatten the left subtree
        leftTail = self.flattenTree(node.left)
        #resursively flatten the right subtree
        rightTail = self.flattenTree(node.right)
        #if there was a left subtree, we shuffle the connections around so that there is nothing on the left side anymore
        if leftTail:
            leftTail.right = node.right
            node.right = node.left
            node.left = None
        
        #we need to return the right mode node after we are done wiring the new connections
        return rightTail if rightTail else leftTail

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.flattenTree(root)