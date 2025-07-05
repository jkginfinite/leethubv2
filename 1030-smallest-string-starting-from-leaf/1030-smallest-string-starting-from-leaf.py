# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        chars = list('abcdefghijklmnopqrstuvwxyz')
        if not root:
            return ''
        minStr = None
        stack = [(root,chars[root.val])]
        while stack:
            node,path = stack.pop()
            if not node.left and not node.right:
                #paths.append(path)
                if not minStr:
                    minStr = path
                else:
                    minStr = min(minStr,path)
            if node.left:
                stack.append((node.left,chars[node.left.val]+path))
            if node.right:
                stack.append((node.right,chars[node.right.val]+path))
        return minStr