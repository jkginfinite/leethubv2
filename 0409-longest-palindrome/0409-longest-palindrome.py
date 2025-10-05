class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd_freq_chars_count = 0
        frequency_map = {}

        for c in s:
            if c not in frequency_map:
                frequency_map[c]=0
            frequency_map[c]+=1

            if frequency_map[c]%2==1:
                odd_freq_chars_count+=1
            else:
                odd_freq_chars_count-=1
        
        if odd_freq_chars_count>0:
            return len(s)-odd_freq_chars_count+1
        else:
            return len(s)