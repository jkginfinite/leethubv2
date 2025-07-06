# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        
        results = []
        stack = [root]
        while stack:
            node = stack.pop()
            results.append(node.val)
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        if len(results)<2:
            return False
        else:
            for index1 in range(len(results)):
                a = results[index1]
                for index2 in range(index1+1,len(results)):
                    b = results[index2]
                    if a+b==k:
                        return True
        return False
        