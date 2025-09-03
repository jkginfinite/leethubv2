class Solution:
    def fixedPoint(self, arr: List[int]) -> int:

        Minn = float('inf')
        for index, i in enumerate(arr):
            if arr[index]==index:
                Minn = min(Minn,index)
        if Minn!=float('inf'):
            return Minn
        return -1
        