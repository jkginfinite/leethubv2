class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:

        #d = {}
        D = []
        for row in range(0,rows):
            for col in range(0,cols):
                distance = abs(row-rCenter)+abs(col-cCenter)
                #d[distance] = [row,col]
                D.append([row,col,distance])

        D = sorted(D,key=lambda x: x[2])
        return [[j[0],j[1]] for j in D]