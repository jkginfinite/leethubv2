class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==1:
            return True
        if n%4!=0 or n<4:
            return False
        while n>4:
            n = n//4
            if n%4!=0:
                return False
        return True
        