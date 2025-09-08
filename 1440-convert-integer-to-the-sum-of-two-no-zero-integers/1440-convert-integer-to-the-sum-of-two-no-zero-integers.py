class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        a = 1
        while not ('0' not in str(n-a) and '0' not in str(a)):
            a+=1
        return [a,n-a]        