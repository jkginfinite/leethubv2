class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        from itertools import permutations
        perms = [int(''.join([str(k) for k in list(j)])) for j in permutations(digits,3)]
        count = 0
        counted = set()
        def helper(perms,count,counted):
            if not perms: #some criteria
                return count
            else:
                val = perms.pop(0)
                if val%2==0 and val>=100 and val not in counted:
                    count+=1
                    counted.add(val)
                else:
                    counted.add(val)
                return helper(perms,count,counted)
        
        return helper(perms, count, counted)
