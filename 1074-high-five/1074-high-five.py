class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        items = sorted(items,key=lambda x: (x[0],x[-1]),reverse=True)

        d = {}
        for i in items:
            if i[0] not in d:
                d[i[0]]=[]
            if len(d[i[0]])<5:
                d[i[0]].append(i[1])
        L = []
        import numpy
        d = dict(sorted(d.items()))
        for key,value in d.items():
            _ = [key,int(numpy.floor(sum(value)/len(value)))]
            L.append(_)
        return L

        """L=[]
        _ = items[0][1]
        count=0
        for index in range(1,len(items)):
            curr = items[index]
            last = items[index-1]
            if curr[0]==last[0] and count<5:
                _+=curr[1]
                count+=1
            elif curr[0]==last[0] and count==5:
                
            else:
                L.append([last[0],_//5])
                count=0
                _="""
        print(items)