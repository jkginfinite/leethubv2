class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # we initialize the dp array with 0s
        # if s[i]=) and s[i-1]=( then dp[i]=dp[i-2]+2
        #we do so beacue the ending () portion is a valid substring anyhow and leads to an increment of 2 in the length of the just previous valid substrings length
        # s[i]=')' and s[i-1]=')'
        # if s[i-dp[i-1]-1]='(' then 
        #dp[i] = dp[i-1]+dp[i-dp[i-1]-2]+2
        maxans = 0
        dp = [0]*len(s)
        for i in range(1,len(s)):
            if s[i]==")":
                if s[i-1]=="(":
                    dp[i] = (dp[i-2] if i>=2 else 0)+2
                elif i-dp[i-1]>0 and s[i-dp[i-1]-1]=="(":
                    dp[i]=(dp[i-1]+(dp[i-dp[i-1]-2] if i-dp[i-1]>=2 else 0)+2)
                maxans = max(maxans,dp[i])
        return maxans