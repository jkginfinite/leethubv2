# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #start from the root node and traverse the tree
        #until we find p and q, keep storing the parent pointers
        #ocne weve found both p and q, we get all the ancestors for p using the parent dictionary and add to a set
        #called ancestors
        #similarly, we traverse through ancestors for node q. the ancestors is present in the ansestors for p
        #this means the first ansestor common between p and q and hance LCA node

        stack = [root]
        parent = {root:None}

        while p not in parent or q not in parent:
            node = stack.pop()

            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right]= node
                stack.append(node.right)
            
        #ancestors set() for node p
        ancestors = set()

        #process all ancestors for node p using parent pointers
        while p:
            ancestors.add(p)
            p = parent[p]

        while q not in ancestors:
            q = parent[q]
        return q
        