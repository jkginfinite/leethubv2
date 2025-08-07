"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        """while p.parent is not None or q.parent is not None:
            if p.val==q.val:
                return q
            if p.parent:
                p=p.parent
            if q.parent:
                q=q.parent
        return None"""

        def samepath(p,q):
            stack = [p]
            while stack:
                node = stack.pop()
                if node==q:
                    return p
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            return None

        if samepath(p,q) is not None:
            print("execute1")
            return samepath(p,q)
        if samepath(q,p) is not None:
            print("execute2")
            return samepath(q,p)

        ancestors = set()
        while p.parent:
            ancestors.add(p)
            p = p.parent

        while q not in ancestors and q.parent:
            q = q.parent
        return q
        

        