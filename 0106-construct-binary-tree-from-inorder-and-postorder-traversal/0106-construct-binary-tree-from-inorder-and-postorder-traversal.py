# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(in_left, in_right):
            if in_left>in_right:
                return None

            #pick the last element as root
            val = postorder.pop()
            root = TreeNode(val)

            index = idx_map[val]

            #build right subtree
            root.right = helper(index+1,in_right)
            #build left subtree
            root.left = helper(in_left,index-1)
            return root
        
        #build a hashmap value
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return helper(0,len(inorder)-1)