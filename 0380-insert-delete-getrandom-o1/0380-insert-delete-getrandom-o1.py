import random
class RandomizedSet:

    def __init__(self):
        self.s = list()
        

    def insert(self, val: int) -> bool:
        if val not in self.s:
            self.s.append(val)
            return True
        return False


    def remove(self, val: int) -> bool:
        if val in self.s:
            self.s.remove(val)
            return True
        return False
        

    def getRandom(self) -> int:
        return random.choice(self.s)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()