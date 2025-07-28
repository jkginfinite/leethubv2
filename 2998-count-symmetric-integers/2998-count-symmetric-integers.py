class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count=0
        for i in range(low,high+1):
            if len(str(i))%2==0:
                _ = str(i)
                left = [int(i) for i in _[:len(_)//2]]
                right = [int(i) for i in _[len(_)//2:]]
                print(left)
                print(right)
                if sum(left)==sum(right):
                    count+=1
        return count
        