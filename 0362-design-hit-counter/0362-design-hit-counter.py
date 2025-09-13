class HitCounter:

    def __init__(self):
        self.record = {}
        

    def hit(self, timestamp: int) -> None:
        if timestamp in self.record:
            self.record[timestamp]+=1
        else:
            self.record[timestamp]=1
        #for key in self.record.keys():
        #    if timestamp-key>300:
        #        del self.record[key]

    def getHits(self, timestamp: int) -> int:
        count=0
        for key in self.record.keys():
            if timestamp-key<300:
                count+=self.record[key]
        return count
# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)