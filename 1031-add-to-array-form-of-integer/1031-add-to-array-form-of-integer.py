class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        import sys
        sys.set_int_max_str_digits(100000)
        n = int(''.join([str(v) for v in num]))
        n+=k
        return [int(j) for j in list(str(n))]
        