class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        #sliding window approach
        #move the right pointer while the window contains not more than two distinct characters
        #if we get more than 3 characters, move the left pointer
        #move the sliding window on the string so we always have only at most 2 distinct characters in the window
        #retrun n if the string length N is smaller than 3
        if len(s)<=2:
            return len(s)
        
        #set both pointers at the beginning of the string, left=0, right=0 and init max_substring length=2
        left=0
        right=0
        S = list(s)
        max_len = 0
        while right<len(s):
            window = S[left:right+1]
            if len(set(window))<=2:
                right+=1
                max_len = max(max_len,len(window))
            else:
                left+=1
        return max_len