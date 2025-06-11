class Solution:
    def isPalindrome(self, x):
        return x==x[::-1]
    def removePalindromeSub(self, s: str) -> int:
        if not s:
            return 0
        if self.isPalindrome(s):
            return 1
        return 2