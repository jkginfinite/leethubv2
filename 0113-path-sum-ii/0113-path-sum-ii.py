# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        def helper(node,RemainingSum,path,pathsList):
            if not node:
                return
            
            path.append(node.val)

            if RemainingSum==node.val and not node.left and not node.right:
                pathsList.append(list(path))
            else:
                helper(node.left,RemainingSum-node.val,path,pathsList)
                helper(node.right,RemainingSum-node.val,path,pathsList)
            
            #we need to pop the node once we are done processing all of its subtrees
            path.pop()

        pathsList = []
        path = []
        Sum = 0
        RemainingSum = targetSum-Sum
        helper(root,RemainingSum,path,pathsList)
        return pathsList

            