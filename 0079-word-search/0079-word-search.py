class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.ROWS = len(board)
        self.COLS = len(board[0])
        self.board = board

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.backtrack(row,col,word):
                    return True
        return False

    
    def backtrack(self,row,col,suffix) -> bool:
        if len(suffix)==0:
            return True

        #check current status before jumping into backtracking
        if (row<0 or row==self.ROWS or col<0 or col==self.COLS or self.board[row][col]!=suffix[0]):
            return False

        ret=False
        #mark the choice before exploring further
        self.board[row][col] = "#"
        #explore the 4 neighbor directions
        for rowOffset, colOffset in [(0,1),(1,0),(0,-1),(-1,0)]:
            ret = self.backtrack(row+rowOffset, col+colOffset, suffix[1:])
            #break instead of return directly to do some clean up afterwards
            if ret:
                break
        
        #revert the change, a clean slate and no side effect
        self.board[row][col]=suffix[0]

        #tried all direction and no match
        return ret
        