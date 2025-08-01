class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        Left_L = [None for i in range(N)]
        Left_L[0] = 1
        Right_R = [None for i in range(N)]
        Right_R[0] = 1
        for index in range(1,N):
            numsL = nums[index-1]
            numsR = nums[-(index)]
            Left_L[index] = numsL*Left_L[index-1]
            Right_R[index] = numsR*Right_R[index-1]

        
        L = []
        for index in range(N):
            _ = Left_L[index]*Right_R[N-index-1]
            L.append(_)
        return L
        
        #left = [1,1,2,6]
        #right = [24,12,4,1]