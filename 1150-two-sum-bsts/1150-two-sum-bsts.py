# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:

        def return_path(root1):
            if not root1:
                return []
            path1 = []
            stack1 = [root1]
            while stack1:
                node = stack1.pop()
                path1.append(node.val)
                if node.left:
                    stack1.append(node.left)
                if node.right:
                    stack1.append(node.right)
            return path1

        path1 = return_path(root1)
        path2 = return_path(root2)

        for i in path1:
            if target - i in path2:
                return True
        return False