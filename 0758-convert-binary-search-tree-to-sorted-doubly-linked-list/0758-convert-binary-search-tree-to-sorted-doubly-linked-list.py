class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        stack = []
        current = root
        first = last = None

        while stack or current:
            # Traverse left subtree
            while current:
                stack.append(current)
                current = current.left

            # Visit node
            current = stack.pop()

            if last:
                last.right = current
                current.left = last
            else:
                first = current  # First node will be the smallest (leftmost)

            last = current

            # Traverse right subtree
            current = current.right

        # Close the doubly linked list
        last.right = first
        first.left = last

        return first
