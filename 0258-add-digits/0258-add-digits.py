class Solution:
    def addDigits(self, num: int) -> int:

        def recursions(num):
            if len(str(num))==1:
                return num
            numm = 0
            for i in str(num):
                numm+=int(i)
            return recursions(numm)
        
        return recursions(num)
        