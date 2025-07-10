class Solution:
    def bfs(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)==1:
            return intervals

        merged = []
        queue = sorted(intervals)
        while queue:
            node1 = queue.pop(0)
            if queue:
                node2 = queue[0]
                if node1[-1]>=node2[0]:
                    interval = [min(node1+node2),max(node1+node2)]
                    merged.append(interval)
                    queue.pop(0)
                else:
                    merged.append(node1)
            else:
                merged.append(node1)
        return merged
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        def recursion(intervals):
            queue = self.bfs(intervals)
            if len(queue)==1:
                return queue
            for index in range(1,len(queue)):
                elemen_next = queue[index]
                elemen = queue[index-1]
                if elemen[-1]>=elemen_next[0]:
                    return recursion(queue)
            return queue
        return recursion(intervals)
