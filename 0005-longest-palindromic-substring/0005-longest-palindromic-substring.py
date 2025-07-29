class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        #1 initialize n=s.length and a boolean table dp with size n*n with all values false
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        #2 initialize [0,0] as the inclusive bounds of the answer
        ans = [0,0]

        #3 where ever i=j set these values to true
        for i in range(n):
            dp[i][i]=True

        #4 Iterate over all pairs, i, i+1. For each one if s[i]==s[i+1] then set dp[i][i+1]=true
        # update ans=[i,i+1]
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                ans = [i,i+1]

        #5 now we populate the dp table. iterate over diff from 2 until n. this variable represents the different j-1
        for diff in range(2,n):
            for i in range(n-diff): #in a nestd for loop iterate over i from 0 until n-diff
                j=i+diff
                if s[i]==s[j] and dp[i+1][j-1]:
                    dp[i][j]=True
                    ans = [i,j]
        #7 retrieve the answer bounds from ans as i,j return the substring of s starting at index i,ending with j
        i,j=ans
        return s[i:j+1]