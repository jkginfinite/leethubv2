# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if not root:
            return []
        
        queue = deque([root])
        diff = inf
        value = None
        while queue:
            node = queue.popleft()
            if abs(target-node.val)<diff:
                value = node.val
                diff = abs(target-node.val)

            elif abs(target-node.val)==diff and value!=node.val:
                value = min(value,node.val)
                diff = abs(target-node.val)
                 
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return value
        