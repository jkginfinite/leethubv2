class Solution:
    def isUgly(self, n: int) -> bool:
        if n==0:
            return False
        factors = [2,3,5]
        working_factors = []
        for i in factors:
            if n%i==0:
                working_factors.append(i)

        for w in working_factors:
            n = n//w
            
        if n==1:
            return True
        else:
            working_factors2 = []
            for w in working_factors:
                if n%w==0:
                    working_factors2.append(w)
            
            for w2 in working_factors2:
                while n%w2==0:
                    n=n//w2
                if n==1:
                    return True
            return False
