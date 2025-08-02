class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #the idea behind the hashmap is as follows. if the cumulative sum
        #represented by sum[i] for sum up to the ith index os the same, the sum f the elements lying in
        #between those those indices

        '''
        we use a hashmap map which is used to sstore the cumulative sum up to all the indices
        possible along with the number of times the same sum occurs. we store the data in the form
        sumi, num of occurrences of sum i. we traverse over the array nums and keep on finding the cumulative sum. every time we encounter a new sum we make anew entry in the hashmap corresponding to that sum
        if the same sum occurs again, we increment the count corresponding to that sum in the hashmap. 
        for every sum we encounter also determine the number of times the sum-k has occurred already, since it will deterine the number of times a subarray with sum k has occurred up to the current index. we increment by count by the same amount
        '''
        count = 0
        total = 0
        hashmap = {0:1}
        for i in nums:
            total+=i
            if total-k in hashmap:
                count+=hashmap[total-k]
            if total not in hashmap:
                hashmap[total]=0
            hashmap[total]+=1
        return count

        