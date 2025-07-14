class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num in [0,1]:
            return True
        if num in [2,3]:
            return False
        def binarySearch(num):
            low=1
            high=num
            x = num
            while low<=high:
                mid = low + (high-low)//2
                if mid+1<=num and mid-1>=0:
                    if mid**2==x:
                        return True
                    elif ((mid+1)**2)>x and ((mid-1)**2)<x and (mid**2)!=x:
                        return False
                    elif (mid**2)<x:
                        low=mid+1
                    else:
                        high = mid-1
                elif mid+1==num:
                    mid-=1
                elif mid-1==0:
                    mid+=1
        return binarySearch(num)