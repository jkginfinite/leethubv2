class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        import numpy
        S = list(s)
        T = list(t)
        summ = 0
        for i in range(len(s)):
            s_char = S[i]
            #t_char = T[i]

            summ+=abs(i - T.index(s_char))
        return summ
        