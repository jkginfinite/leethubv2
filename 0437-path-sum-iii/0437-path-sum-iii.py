# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def helper(node,currSum):
            nonlocal count
            if not node:
                return

            currSum+=node.val

            if currSum==targetSum:
                count+=1
            
            count+=hashmap[currSum-targetSum]

            hashmap[currSum]+=1

            helper(node.left,currSum)
            helper(node.right,currSum)

            #remove thecurrent sum from the hashmap in order to not use it during parallel subtree processing
            hashmap[currSum]-=1
        
        count=0
        hashmap = defaultdict(int)
        helper(root,0)
        return count