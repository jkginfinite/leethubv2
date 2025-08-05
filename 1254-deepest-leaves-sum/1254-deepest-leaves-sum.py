# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        level = 0
        Sum = 0
        depth = 0
        queue = [[root,root.val]]

        while queue:
            node,level = queue.pop(0)

            if not node.left and not node.right:
                if depth<level:
                    Sum = node.val
                    depth = level
                elif depth==level:
                    Sum+=node.val

            if node.left:
                queue.append([node.left,level+1])
                #levels[level+1].append(node.left.val)

            if node.right:
                queue.append([node.right,level+1])
                #levels[level+1].append(node.right.val)

        return Sum  