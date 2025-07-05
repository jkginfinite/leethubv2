class Solution:
    def findLucky(self, arr: List[int]) -> int:
        S = set(arr)
        MaxCount = 0
        for i in S:
            count = arr.count(i)
            if count>=1:
                if i==count:
                    MaxCount = max(count,MaxCount)
        if MaxCount==0:
            return -1
        return MaxCount
        