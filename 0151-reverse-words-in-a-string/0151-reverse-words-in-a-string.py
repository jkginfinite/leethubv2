class Solution:
    def reverseWords(self, s: str) -> str:
        arr = [j.strip() for j in s.split(' ') if j!='']
        low =0
        high=len(arr)-1
        while low<high:
            Right = arr[high]
            Left = arr[low]
            arr[low],arr[high] = Right, Left
            high-=1
            low+=1
        return ' '.join(arr)
            