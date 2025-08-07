class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        observe that for any given sequence that is in descending order, no lext larger permutation is possible
        for example no next permutation is possible for 3,2,1

        we need to find the first pair of two successive number a[i] and a[i-1] from the right which
        satisfy a[i]>a[i-1], now no rearrangements to the right of a[i-1] can create a larger permutation
        since that subarrays consists of numbers in descending order
        thus we need to rearrange the numbers to the right of a[i-1] including itsself

        now what kind of rearrangement will produce the next larger number/ we want to create the permuation
        just larger than the current one. therefor we need to replace the number a[i-1] with the number which is just
        larger than itself among the numbers lying to its right section, say a[j]

        we swap the numbers a[i-1] and a[j]. we now have the correct number at index i-1 but still the current permuation isnt the right one. we need the smallest permutation that can be formed by using the numbers only to the right of a[i-1] 

        recall that while scaning the number from the right we simply kept decrementing the index until we found a[i] and a[i-1] where a[i]>a[i-1]. thus all numbers to the right of a[i-1] were already sorted in descending order

        158476531

        find first decreaing element

        4 is the first decreasing element

        158 4 -> 76 5 31 swap 4<->5, reverse sort the remaining elements


        158513467   
        """
        i = len(nums)-2
        while i>=0 and nums[i+1]<=nums[i]:
            i-=1
        if i>=0:
            j = len(nums)-1
            while nums[j]<=nums[i]:
                j-=1
            self.swap(nums,i,j)
        self.reverse(nums,i+1)

    def reverse(self, nums, start):
        i,j = start,len(nums)-1
        while i<j:
            self.swap(nums,i,j)
            i+=1
            j-=1

    def swap(self,nums,i,j):
        temp=nums[i]
        nums[i]=nums[j]
        nums[j]=temp