class CustomStack:
    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        
    def push(self, x: int) -> None:
        if len(self.stack)<self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        if k>=len(self.stack):
            for index in range(len(self.stack)):
                self.stack[index]+=val
        else:
            for index in range(k):
                self.stack[index]+=val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)