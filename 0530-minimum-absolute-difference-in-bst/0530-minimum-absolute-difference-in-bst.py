# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        import numpy
        if not root:
            return 0
        
        stack = [root]
        results = []

        while stack:
            node = stack.pop()
            results.append(node.val)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        results.sort()
        minDiff = 1e9
        for i in range(1,len(results)):
            minDiff = min(minDiff, results[i]-results[i-1])
        return minDiff
        
                    




