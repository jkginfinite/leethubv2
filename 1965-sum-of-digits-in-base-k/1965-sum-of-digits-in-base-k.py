class Solution:
    def sumBase(self, n: int, k: int) -> int:
        #break n into factors of 10
        digits = []
        while n>0:
            digits.append(int(n%k))
            n = n//k
        return sum(digits)  