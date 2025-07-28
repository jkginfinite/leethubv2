class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        from itertools import permutations
        str_digits = [str(j) for j in digits]
        digits = set([int(''.join(j)) for j in list(permutations(str_digits,3)) if j[0]!=0 and int(''.join(j))>=100 and int(''.join(j))%2==0])
        return sorted(digits)
        