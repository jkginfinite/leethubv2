class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr)-1

        while left<=right:
            pivot = (left+right)//2

            #if number of positive integers whiuch are missing before arr[pivot] is less than k,
            #continue to the right
            if arr[pivot]-pivot-1<k:
                left = pivot + 1
            #otherwise go left
            else:
                right = pivot - 1
                
        return left+k