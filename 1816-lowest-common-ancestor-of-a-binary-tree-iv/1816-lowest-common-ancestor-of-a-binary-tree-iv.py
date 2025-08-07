# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        #step1 build parent map
        parent = {root:None}
        stack = [root]

        while not all(target in parent for target in nodes):
            node = stack.pop()
            for child in (node.left,node.right):
                if child:
                    parent[child]=node
                    stack.append(child)

        #step 2: build ancestor set for first target node
        common = set()
        curr = nodes[0]
        while curr:
            common.add(curr)
            curr = parent[curr]

        #step 3 for each node filter common ancestors
        for target in nodes[1:]:
            seen = set()
            curr = target
            while curr:
                if curr in common:
                    seen.add(curr)
                curr = parent[curr]
            common = common & seen
        
        #step 4 among the remaining common nodes, choose the depest

        def get_depth(node,parent_map):
            depth = 0
            while node:
                node = parent_map[node]
                depth+=1
            return depth
        def deepest_node_in(common_nodes,parent_map):
            return max(common_nodes,key=lambda node: get_depth(node,parent))
        return deepest_node_in(common,parent)
        