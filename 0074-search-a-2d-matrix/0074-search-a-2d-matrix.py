class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binSearchRow(matrix,target):
            low = 0
            high=len(matrix)-1
            while low<=high:
                mid = (high+low)//2
                if matrix[mid][0]<=target and matrix[mid][-1]>=target:
                    return mid
                elif matrix[mid][0]>target:
                    high = mid-1
                else:
                    low=mid+1
            return mid
        
        def binSearchCol(matrix,target,row):
            low=0
            high = len(matrix[row])-1
            while low<=high:
                mid =(high+low)//2
                if matrix[row][mid]==target:
                    return mid
                elif matrix[row][mid]>target:
                    high=mid-1
                else:
                    low=mid+1
            return -1

        if len(matrix)==0 or len(matrix[0])==0:
            return False
        row = binSearchRow(matrix,target)
        if row==-1:
            return False
        col = binSearchCol(matrix,target,row)
        return col!=-1
        
    
        