import numpy
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        #calculate the slope between two points in the list. If the new slope calculate is different from the last slope calculation, return False. Otherwise, return True
        if coordinates[1][0]-coordinates[0][0]!=0:
            m = (coordinates[1][1]-coordinates[0][1])/(coordinates[1][0]-coordinates[0][0])
        elif coordinates[1][0]-coordinates[0][0]==0:
            m = 1e27#numpy.inf
        print(m)
        for index in range(2,len(coordinates)):
            if (coordinates[index][0]-coordinates[index-1][0])!=0:
                _ = (coordinates[index][1]-coordinates[index-1][1])/(coordinates[index][0]-coordinates[index-1][0])
            elif coordinates[index][0]-coordinates[index-1][0]==0:
                _ = 1e27 #numpy.inf
            if _!=m:
                return False
        return True
        