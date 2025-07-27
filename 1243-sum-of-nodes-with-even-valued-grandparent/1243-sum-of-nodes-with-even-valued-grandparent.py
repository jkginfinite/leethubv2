# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self,node):
        if node.val%2==0:
            if node.left:
                if node.left.left:
                    self.score+=node.left.left.val
                if node.left.right:
                    self.score+=node.left.right.val
            if node.right:
                if node.right.left:
                    self.score+=node.right.left.val
                if node.right.right:
                    self.score+=node.right.right.val
        if node.left:
            self.traverse(node.left)
        if node.right:
            self.traverse(node.right)

    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        self.score=0
        self.traverse(root)
        return self.score
        