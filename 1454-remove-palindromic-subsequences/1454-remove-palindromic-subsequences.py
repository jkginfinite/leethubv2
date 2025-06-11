class Solution:
    def isPalindrome(self, s):
        left = 0
        right = len(s)-1
        while left<right:
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True

    def removePalindromeSub(self, s: str) -> int:
        if not s:
            return 0
        if self.isPalindrome(s):
            return 1
        return 2