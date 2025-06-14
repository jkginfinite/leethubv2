# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        from collections import deque
        queue = deque([root])
        loners = []
        while queue:
            node = queue.popleft()
            if node.left and not node.right:
                queue.append(node.left)
                loners.append(node.left.val)
            if node.right and not node.left:
                queue.append(node.right)
                loners.append(node.right.val)
            if node.left and node.right:
                queue.append(node.left)
                queue.append(node.right)
        return loners

