import heapq
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        #use a min heap to store tuples of the sum of soldiers and their respect row indices
        min_heap = []

        #caclualte the sum of soldiers for each row and store in the min heap
        for row in range(len(mat)):
            soldier_count = self.binary_search(mat[row])
            heapq.heappush(min_heap,(soldier_count, row))

        #extract the k weakest row indices
        weakest_rows = []
        for i in range(k):
            weakest_rows.append(heapq.heappop(min_heap)[1])

        return weakest_rows

    def binary_search(self, row):
        left, right = 0, len(row)-1

        #perform binary search to the find the count of soldiers
        while left<=right:
            mid = (left+right)//2
            if row[mid]==1:
                left = mid+1
            else:
                right = mid-1
        return left
