# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:

        #scale down until ArrayReader.get(i)!=2**31-1
        i = int(10**4)
        while reader.get(int(i))==int((2**31)-1):
            i/=2

        while reader.get(int(i))!=int((2**31)-1):
            i+=1
        low = 0
        high = i

        while low<=high:
            mid = int(low+(high-low)//2)
            if reader.get(mid)==target:
                return mid
            if reader.get(mid)>target:
                high = mid-1
            else:
                low = mid+1
        return -1