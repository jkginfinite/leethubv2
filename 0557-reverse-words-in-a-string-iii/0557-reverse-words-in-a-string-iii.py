class Solution:
    def reverseWords(self, s: str) -> str:
        L = s.split(' ')
        LL = []
        for i in L:
            LL.append(i[::-1])
        return ' '.join(LL)