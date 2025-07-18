class Solution:
    def balancedStringSplit(self, s: str) -> int:
        #look for balanced patterns in the string, e.g. RL, RRLL,
        #split on each pattern
        #step 1: create two variables called balanced and return value
        # step 2: loop through each characters in the given string (note that the string will only have L and R),
        # increase variable by one if char is R or decrease by one
        #step 3: if the string is balanced increase the return value
        balance = 0
        ret_val = 0
        for char in s:
            if char=="R":
                balance+=1
            else:
                balance-=1
            if balance==0:
                ret_val+=1
        return ret_val