class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for index1 in range(len(arr)):
            for index2 in range(index1+1,len(arr)):
                if 2*arr[index1]==arr[index2] or arr[index1]==2*arr[index2]:
                    return True
        return False
            