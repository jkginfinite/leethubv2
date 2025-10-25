class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        rows_tot = len(matrix)
        columns_tot = len(matrix[0])
        cols = []
        for col in range(columns_tot):
            _ = []
            for row in range(rows_tot):
                _.append(matrix[row][col])
            cols.append(_)

        print(cols)

        lucky = []
        for row in range(rows_tot):
            for col in range(columns_tot):
                _ = matrix[row][col]
                if _ == min(matrix[row]) and _==max(cols[col]):
                    #print(cols[row])
                    lucky.append(_)
        return lucky 


        