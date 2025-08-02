# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return root

        start,end=1,2

        tailNode = None
        stack = [[root,start]]

        while stack:
            node, state = stack.pop()

            #leaf
            if not node.left and not node.right:
                tailNode = node
                continue
            
            #if node is in the start state, it means we havent processed its left child
            if state==start:
                if node.left:
                    stack.append([node,end])
                    stack.append([node.left,start])
                
                elif node.right:
                    #incase the current node didnt have a left child, append its right child
                    stack.append([node.right,start])
            else:
                #if the current node is in the end state, that means we did process one of its own child
                rightNode = node.right

                if tailNode:
                    #establish the proper connections
                    tailNode.right = node.right
                    node.right = node.left
                    node.left = None
                    rightNode = tailNode.right
                
                if rightNode:
                    stack.append([rightNode,start])

