# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if (not root) or (not subRoot):
            return False
        
        def dfs(node):
            #if this node is empty, then no tree is rooted at this node
            #thus tree rooted at node cannot be the same as rooted at subRoot
            if node is None:
                return False
            
            #if tree rooted at node is identical to tree at rubroot
            elif is_identical(node,subRoot):
                return True

            #if tree rooted at node was no identical check for tree rooted at children
            return dfs(node.left) or dfs(node.right)

        def is_identical(node1,node2):
            #if any node is empty, both should be empty
            if node1 is None or node2 is None:
                return node1 is None and node2 is None

            #both node value shouldbe equal and their respective left and right subtree should be identical
            return (node1.val==node2.val) and is_identical(node1.left, node2.left) and is_identical(node1.right, node2.right)
        
        #chck for node rooted at root
        return dfs(root)