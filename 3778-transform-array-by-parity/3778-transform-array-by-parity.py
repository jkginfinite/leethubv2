class Solution:
    def merge_sort(self,arr):
        if len(arr)<=1:
            return arr
        
        #split array into two halves
        mid = len(arr)//2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])
        return self.merge(left,right)

    def merge(self,left,right):
        sorted_arr = []
        i=j=0

        while i<len(left) and j<len(right):
            if left[i] <= right[j]:
                sorted_arr.append(left[i])
                i+=1
            else:
                sorted_arr.append(right[j])
                j+=1

        sorted_arr.extend(left[i:])
        sorted_arr.extend(right[j:])
        return sorted_arr

    def transformArray(self, nums: List[int]) -> List[int]:
        L = []
        for i in range(len(nums)):
            elem = nums[i]
            if elem%2==0:
                L.append(0)
            else:
                L.append(1)
        
        return self.merge_sort(L)