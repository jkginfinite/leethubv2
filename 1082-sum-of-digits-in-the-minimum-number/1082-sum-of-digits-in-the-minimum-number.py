class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:

        minn = min(nums)

        """
        def recursion(number):
            if len(str(number))==1:
                return number
            numz = 0
            for i in str(number):
                numz+=int(i)
            return recursion(numz)
        """

        if len(str(minn))==1:
            if minn%2!=0:
                return 0
            else:
                return 1
        else:
            numz = 0
            for i in str(minn):
                numz+=int(i)
            if numz%2!=0:
                return 0
            else:
                return 1