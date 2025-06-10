class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        left=0
        right=len(s)-1
        S = list(s)
        if len(s)%2==0:
            while left<right:
                L = S[left]
                R = S[right]
                if L!=R:
                    if L==min(L,R):
                        S[right]=min(L,R)
                    else:
                        S[left]=min(L,R)
                left+=1
                right-=1
        else:
            while left<=(len(s)//2) and right>=((len(s)//2)+1):
                L = S[left]
                R = S[right]
                if L!=R:
                    if L==min(L,R):
                        S[right]=min(L,R)
                    else:
                        S[left]=min(L,R)
                left+=1
                right-=1
        return ''.join(S)

        