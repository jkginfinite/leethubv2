import collections
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = collections.OrderedDict()

    def get(self, key):
        if key not in self.dic:
            return -1
        self.dic.move_to_end(key)
        return self.dic[key]
    
    def put(self, key, value):
        if key in self.dic:
            self.dic.move_to_end(key)

        self.dic[key] = value
        if len(self.dic)>self.capacity:
            self.dic.popitem(False)