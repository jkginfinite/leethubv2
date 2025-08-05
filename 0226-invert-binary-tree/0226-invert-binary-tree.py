# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        queue = [root]
        while queue:
            node = queue.pop(0)

            if node.left and node.right:
                left,right = node.left,node.right
                node.left,node.right = right,left
                queue.append(node.left)
                queue.append(node.right)

            elif node.left:
                left = node.left
                node.right = left
                node.left = None
                queue.append(node.right)
            
            elif node.right:
                right = node.right
                node.left = right
                node.right = None
                queue.append(node.left)
        return root
        