# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:

        def inorder(node):
            stack = []
            result = []
            while node or stack:
                while node:
                    stack.append(node)
                    node=node.left
                if stack:
                    node = stack.pop()
                    result.append(node.val)
                    node = node.right
            return result


        path1 = inorder(root1)
        path2 = inorder(root2)

        i=0
        j=len(path2)-1
        while i<len(path1) and j>=0:
            curr_sum = path1[i]+path2[j]
            if curr_sum==target:
                return True
            elif curr_sum<target:
                i+=1
            else:
                j-=1
        return False