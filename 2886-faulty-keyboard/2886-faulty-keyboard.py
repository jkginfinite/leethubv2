class Solution:
    def finalString(self, s: str) -> str:
        v=''
        for k in s:
            if k=='i':
                v=v[::-1]
            else:
                v+=k
        return v 