# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        #the strategy is to use BFS to traverse both trees simultaneously. If we come upon the target in the original's node, we return the node of the copy
        stack_o = []
        stack_c = []
        node_o = original
        node_c = cloned

        while stack_o or node_c:
            while node_o:
                stack_o.append(node_o)
                stack_c.append(node_c)

                node_o = node_o.left
                node_c = node_c.left
            
            node_o = stack_o.pop()
            node_c = stack_c.pop()

            if node_o is target:
                return node_c
            
            node_o = node_o.right
            node_c = node_c.right