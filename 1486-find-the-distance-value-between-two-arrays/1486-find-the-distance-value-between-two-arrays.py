class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        count=0
        for i in arr1:
            c = 0
            for j in arr2:
                if abs(i-j)<=d:
                    c +=1
                    continue
            if c>0:
                count+=1
        return len(arr1)-count