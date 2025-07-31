class TwoSum:
    def __init__(self):
        self.nums = []
        self.is_sorted = False
        

    def add(self, number: int) -> None:
        self.nums.append(number)
        self.is_sorted = False

    def find(self, value: int) -> bool:
        if self.is_sorted==False:
            self.nums.sort()
            self.is_sorted=True
        low = 0
        high = len(self.nums)-1
        while low<high:
            sum = self.nums[low]+self.nums[high]
            if sum<value:
                low+=1
            elif sum>value:
                high-=1
            else:
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)