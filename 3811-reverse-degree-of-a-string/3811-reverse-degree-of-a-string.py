class Solution:
    def reverseDegree(self, s: str) -> int:
        l = list('abcdefghijklmnopqrstuvwxyz')
        Sum = 0
        for index,i in enumerate(s):
            Sum+=((26-l.index(i))*(index+1))
            #print(26-l.index(i))
        return Sum

