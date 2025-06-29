class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def helper(n):
            if n%3!=0:
                return False
            elif n==3:
                return True
            else:
                return helper(n//3) #tail recursion
        if n==1:
            return True
        if n<=0 or n%3!=0:
            return False
        else:
            return helper(n)
            

        