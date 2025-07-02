class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==1:
            return True
        if n%4!=0 or n<4:
            return False
        def recursive(n):
            if n%4!=0:
                return False
            elif n<=4:
                return True
            return recursive(n//4) #tail recursion
        return recursive(n)

        