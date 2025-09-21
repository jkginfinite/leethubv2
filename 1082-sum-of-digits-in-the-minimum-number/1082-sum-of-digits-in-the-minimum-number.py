class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:

        minn = min(nums)
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