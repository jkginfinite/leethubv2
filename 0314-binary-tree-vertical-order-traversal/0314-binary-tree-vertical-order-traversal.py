# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #use breadth first search to find levels
        #sort the levels accordingly
        if not root:
            return []
        from collections import deque

        level = 0
        queue = [[root,level]]
        #queue = deque([(root,level)])
        levels = {0:[root.val]}
        while queue:
            (node,level) = queue.pop(0)#popleft()
                
            if node.left:
                queue.append([node.left,level-1])
                if level-1 not in levels:
                    levels[level-1]=[]
                levels[level-1].extend([node.left.val])
            if node.right:
                queue.append([node.right,level+1])
                if level+1 not in levels:
                    levels[level+1]=[]
                levels[level+1].extend([node.right.val])

        s = sorted(levels.items())
        L = []
        for v in s:
            L.append(v[1])
        return L