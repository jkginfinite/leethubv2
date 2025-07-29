class Solution:
    def reverse(self, x: int) -> int:
        s = ''
        negative=False
        for i in str(x):
            if i not in ['-','+']:
                s = i+s
            elif i=='-':
                negative=True
        S = int(s)
        if negative:
            S = -S
        if S>(2**31)-1 or S<-2**31:
            return 0
        return S
        