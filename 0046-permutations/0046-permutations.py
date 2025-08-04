class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''to generate a permuation on element at a time, we will use an array
        curr that represents the current permuation we are building. To start
        we add the first element in nums. we have curr = [nums[0]]. now we find all permuations with 
        nums[0].

        to find all permuations with nums[0] we start by adding the next element/
        now we have curr = [nums[0],nums[1]]

        we are locking in this second element and we will now findall permuations that start with nums[0] and nums[1]. this continues until we use all emenets, curr.length==nums.length

        lets say we have finished finding all permutions that start with [nums[0],nums[1]]. Now what?
        we have to backtrack by removing the nums[1] and we have curr=nums[0] again. now we add the second element that comes after nums[0] which is nums[2], 
        we have curr=nums[0],nums[2] and now we find all permuations that start with [nums[0],nums[2]]
        one we find all the permuations of nums[0] we back track by removing nums[0] from curr and adding the next element, curr=[nums[1]]. now we find all the permuations with number [1]
        '''

        def backtrack(curr):
            if len(curr)==len(nums):
                ans.append(curr[:])
                return
            
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()
        ans = []
        backtrack([])
        return ans

        