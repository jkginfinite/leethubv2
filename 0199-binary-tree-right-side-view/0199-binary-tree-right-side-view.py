# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
    
        level=0
        queue = [(root,level)]
        levels = {level:[root.val]}
        
        while queue:
            node,level = queue.pop(0)
            if level+1 not in levels and node.left or node.right:
                levels[level+1]=[]
            if node.left:
                queue.append([node.left,level+1])
                levels[level+1].extend([node.left.val])
            if node.right:
                queue.append([node.right,level+1])
                levels[level+1].extend([node.right.val])
        L=[]
        for value in levels.values():
            if len(value)==1:
                L.append(value[0])
            elif len(value)>1:
                L.append(value[-1])
        return L