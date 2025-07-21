import re
class Solution:
    def validPalindrome(self, s):
        return s==s[::-1]
    
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]','',s.lower())
        s = s.replace(' ','')
        return self.validPalindrome(s)