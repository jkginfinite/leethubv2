# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def linkedlist_to_list(head):
            L = []
            while head:
                L.append(head.val)
                head = head.next
            return L

        def sortedArrayToBST(nums):
            def helper(left,right):
                if left>right:
                    return None
                
                p = (left+right)//2
                tree = TreeNode(nums[p])
                tree.left = helper(left,p-1)
                tree.right = helper(p+1,right)
                return tree
            return helper(0,len(nums)-1)

        nums = linkedlist_to_list(head)    
        return sortedArrayToBST(nums)
        