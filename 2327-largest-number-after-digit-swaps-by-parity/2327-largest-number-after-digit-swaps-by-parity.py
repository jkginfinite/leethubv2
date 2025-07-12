class Solution:
    def largestInteger(self, num: int) -> int:
        odd_heap = []
        even_heap = []
        num = str(num)

        for char in num:
            if int(char)%2==0:
                heapq.heappush(even_heap,-int(char))
            else:
                heapq.heappush(odd_heap,-int(char))
        
        res = []
        for i in range(len(num)):
            if int(num[i])%2==0:
                digit = -heapq.heappop(even_heap)
            else:
                digit = -heapq.heappop(odd_heap)
            res.append(str(digit))
        return int("".join(res))

