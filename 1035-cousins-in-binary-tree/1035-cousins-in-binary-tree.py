# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        

        def depth_parents(node,val):
            depth = 0
            queue = [(node,depth)]
            while queue:
                node,depth = queue.pop(0)
                if node.val==val:
                    return (node.val,depth)
                if node.left:
                    if node.left.val==val:
                        return (node.val,depth+1)
                    queue.append((node.left,depth+1))
                if node.right:
                    if node.right.val==val:
                        return (node.val,depth+1)
                    queue.append((node.right,depth+1))

        parentX, depthX = depth_parents(root,x)
        parentY, depthY = depth_parents(root,y)
        return (parentX!=parentY) and (depthX==depthY)

        