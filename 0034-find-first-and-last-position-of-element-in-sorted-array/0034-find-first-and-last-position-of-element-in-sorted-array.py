class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(arr,low,high,x):
            while low<=high:
                mid = low+(high-low)//2
                if arr[mid]==x:
                    #now we've found the an instance of x in the array:
                    #we seek to the first and last instance of it
                    print("mid: ",mid)
                    midL, midR = mid,mid
                    if midR+1<len(arr):
                        while midR+1<len(arr) and arr[midR]==arr[midR+1]:
                            print('midR while')
                            midR+=1
                        
                        
                    if midL-1>=0:
                        while midL-1>=0 and arr[midL-1]==arr[midL]:
                            print('midL while')
                            midL-=1

                    return [midL,midR]
                elif arr[mid]<x:
                    low = mid+1
                else:
                    high = mid-1
            return [-1,-1]
        return binarySearch(nums,0,len(nums)-1,target)
        