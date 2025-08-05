# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        node_list = []

        def bfs(root):
            queue = [[root,0,0]]
            while queue:
                node, row, column = queue.pop(0)
                if node is not None:
                    node_list.append([column,row,node.val])
                    queue.append([node.left,row+1,column-1])
                    queue.append([node.right,row+1,column+1])
        
        bfs(root)
        node_list.sort()
        ret = OrderedDict()
        for column, row, value in node_list:
            if column in ret:
                ret[column].append(value)
            else:
                ret[column]=[value]
        return list(ret.values())        