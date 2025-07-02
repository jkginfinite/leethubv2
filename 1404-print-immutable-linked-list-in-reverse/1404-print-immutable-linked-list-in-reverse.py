# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        if head is not None:
            #if head.printValue() line is above the recursive function, it prints
            #normally
            self.printLinkedListInReverse(head.getNext()) 
            head.printValue()
            #if head.printValue() line is below the recursive function, it prints in reverse