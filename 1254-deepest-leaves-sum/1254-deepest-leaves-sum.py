# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            return root.val

        level = 0
        levels={level:[root.val]}
        queue = [[root,root.val]]

        while queue:
            node,level = queue.pop(0)

            if node.left or node.right:
                if level+1 not in levels:
                    levels[level+1]=[]

            if node.left:
                queue.append([node.left,level+1])
                levels[level+1].append(node.left.val)

            if node.right:
                queue.append([node.right,level+1])
                levels[level+1].append(node.right.val)

        return sum(levels[level])    