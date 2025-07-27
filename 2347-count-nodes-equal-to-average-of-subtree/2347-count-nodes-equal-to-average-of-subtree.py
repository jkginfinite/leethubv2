# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        if not root:
            return 0

        res = 0
        stack = [(root, False)]
        node_info = {}  # node -> (sum, count)

        while stack:
            node, visited = stack.pop()

            if node is None:
                continue

            if visited:
                # Post-order: compute the sum and count
                left_sum, left_count = node_info[node.left] if node.left else (0, 0)
                right_sum, right_count = node_info[node.right] if node.right else (0, 0)

                total_sum = left_sum + node.val + right_sum
                total_count = left_count + 1 + right_count

                if total_sum // total_count == node.val:
                    res += 1

                node_info[node] = (total_sum, total_count)
            else:
                # First push the node again as visited
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))

        return res
