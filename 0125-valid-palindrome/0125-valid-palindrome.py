import re
class Solution:    
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]','',s.lower())
        s = s.replace(' ','')
        return s==s[::-1]