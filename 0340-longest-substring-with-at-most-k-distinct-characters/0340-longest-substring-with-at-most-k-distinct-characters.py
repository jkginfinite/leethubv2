class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if len(s)<k:
            return len(s)

        left=0
        right=0
        S = list(s)
        max_len = 0
        while right<len(s):
            window = S[left:right+1]

            if len(set(window))<=k:
                max_len = max(max_len,len(window))
                right+=1
            elif len(set(window))>k:
                left+=1
        
        return max_len