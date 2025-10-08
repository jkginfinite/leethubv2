class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n = int(num1)+int(num2)
        import sys
        sys.set_int_max_str_digits(10000)
        return str(n)
        