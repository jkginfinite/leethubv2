class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #initalize an array sub which contains the first element of nums
        #iterate through the input, starting at the second element
        #for each element num
        #if num is greater than any element in sub then add num to sub
        #otherwise perform a binary search in sub to find the smallest element that is greater than or
        #equal to num and replace that element with num
        sub = []
        for num in nums:
            i = bisect_left(sub,num)
            #if num is greater than any element in sub
            if i==len(sub):
                sub.append(num)

            #other wise replace the first element in sub greater than or equal to num
            else:
                sub[i]=num
        return len(sub)