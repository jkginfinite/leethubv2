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
        import numpy
        mindiff = numpy.inf
        if len(results)>2:
            for index1 in range(len(results)):
                L = results[index1]
                for index2 in range(index1+1,len(results)):
                    R = results[index2]
                    mindiff = min(abs(R-L),mindiff)
            return mindiff
        else:
            return abs(max(results)-min(results))
        
                    




