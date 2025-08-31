class Solution:
    def binarySearch(self,nums,target):
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = (left+right)//2

            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left = mid+1
            else:
                right = mid-1
        return -1

    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        chars = "abcdefghijklmnopqrstuvwxyz"
        nums = list(range(26))
        d = dict(zip(chars,nums))
        D = dict(zip(nums,chars))
        LETTERS = set()
        for l in letters:
            LETTERS.add(d[l])
        TARGET = d[target]
        LETTERS = sorted(list(LETTERS))
        search = self.binarySearch(LETTERS,TARGET)

        if search!=-1:
            if search+1 < len(LETTERS):
                return D[LETTERS[search+1]]
            else:
                return letters[0]
        if search==-1:
            if TARGET>=max(LETTERS) or TARGET<min(LETTERS):
                return letters[0]
            else:
                left = 0
                right = len(LETTERS)-1
                while left<=right:
                    mid = (left+right)//2
                    if LETTERS[mid]<TARGET and LETTERS[mid+1]>TARGET:
                        return D[LETTERS[mid+1]]
                    elif LETTERS[mid]<TARGET:
                        left = mid+1
                    else:
                        right = mid-1
            

        