class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)-1
        n = len(grid[0])-1
        def getneighbors(row,col):
            neighbors = []
            if row+1<=m:
                neighbors.append([row+1,col])
            if row-1>=0:
                neighbors.append([row-1,col])
            if col+1<=n:
                neighbors.append([row,col+1])
            if col-1>=0:
                neighbors.append([row,col-1])
            return neighbors
        
        islands = 0
        for row_index in range(m+1):
            for col_index in range(n+1):
                if grid[row_index][col_index]=="1":
                    #find all cells associated with this island
                    stack = [[row_index,col_index]]
                    islands+=1
                    while stack:
                        r,c = stack.pop()
                        grid[r][c]="0"
                        for neighbor in getneighbors(r,c):    
                            rr,cc = neighbor
                            if grid[rr][cc]=='1':
                                stack.append(neighbor)

        return islands