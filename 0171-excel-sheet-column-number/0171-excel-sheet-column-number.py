class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        s = 'abcdefghijklmnopqrstuvwxyz'.upper()
        S = list(s)
        N = len(S)
        d = dict(zip(S,range(1,N+1)))
        
        position = 0

        ct = list(columnTitle)
        N_ct = len(columnTitle)-1
        for index in range(len(ct)-1,-1,-1):

            element = ct[index]
            value = d[element]*(26**(N_ct-index))
            position+=value
            print(value)
            print(position)
        return position