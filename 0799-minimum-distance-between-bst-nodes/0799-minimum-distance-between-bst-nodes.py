# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1

        #use in order DFS, save the sorted values, then find the minimum difference between nodes
        #in order BST
        results = []
        stack = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            results.append(current.val)
            current = current.right

        min_val = 1e100
        for index1 in range(1,len(results)):
            diff = abs(results[index1]-results[index1-1])
            min_val = min(min_val,diff)
        return min_val