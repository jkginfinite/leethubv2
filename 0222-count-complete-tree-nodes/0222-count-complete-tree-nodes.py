# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        #BFS iterative
        result = 0
        if not root:
            return result
        
        queue = [root]

        while queue:
            node = queue.pop(0)
            result+=1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

        