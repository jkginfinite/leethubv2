class Solution:
    def minOperations(self, nums: List[int]) -> int:
        #create a hashmap object named counter to count the occurrences of each element in the given array nums
        #initialize a variable ans=0 tokeep track of the minimum number of operations required
        #for each value c in the counter's values
        #check if c is equal to 1. if yes, return -1, as it is not possible to perform the required operations
        #on a single element
        #else increment the answer
        counter = Counter(nums)
        ans = 0
        for c in counter.values():
            if c==1:
                return -1
            ans+=ceil(c/3)
        return ans