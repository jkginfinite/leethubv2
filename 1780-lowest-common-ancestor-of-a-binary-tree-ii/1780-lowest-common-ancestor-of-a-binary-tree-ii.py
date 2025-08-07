# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def returnLCA(root,p,q):
            stack=[root]
            parents={root:None}
            while p not in parents or q not in parents:
                node = stack.pop()
                if node.left:
                    parents[node.left]=node
                    stack.append(node.left)
                if node.right:
                    parents[node.right]=node
                    stack.append(node.right)
            ancestors=set()
            while p:
                ancestors.add(p)
                p = parents[p]
            while q not in ancestors:
                q=parents[q]
            return q

        results = []
        stack = [root]
        while stack:
            node = stack.pop()
            results.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        if p.val not in results or q.val not in results:
            return None
        return returnLCA(root,p,q)