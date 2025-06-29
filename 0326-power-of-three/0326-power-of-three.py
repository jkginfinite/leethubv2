class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==1:
            return True
        if n<=0 or n%3!=0:
            return False

        else:
            #must be divisible by only 3
            while n>3:
                print("n: ",n)
                print("n//3: ",n//3)
                n = n//3
                if n%3!=0:
                    return False
            return True

        