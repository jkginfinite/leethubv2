class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        full_set = list(range(1,max(arr)+k+1))

        count=0
        for n in full_set:
            if n not in arr:
                count+=1
            if count==k:
                return n