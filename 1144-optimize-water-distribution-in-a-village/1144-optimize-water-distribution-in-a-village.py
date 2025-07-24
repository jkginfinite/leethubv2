#sort all the edges based on their costs, including additional edges that are added with the virtual vertex
#iterate through the sorted edges. For each edge, if both ends of the edge belong to different groups, with the help of the union Find data structure, we then add this edge into the final minimum spanning tree
class UnionFind:
    def __init__(self,size):
        self.group = [i for i in range(size+1)]
        #the rank of each node for later rebalancicng
        self.rank = [0]*(size+1)
    
    def find(self, person):
        """
        return the group id that person belongs to
        """
        if self.group[person]!=person:
            self.group[person]=self.find(self.group[person])
        return self.group[person]

    def union(self, person_1, person_2):
        """
        join the groups together
        return false when two groups belong to the same group already, otherwise true
        """
        group_1 = self.find(person_1)
        group_2 = self.find(person_2)

        if group_1==group_2:
            return False

        #attach the group of lower rank to the group with higher rank
        if self.rank[group_1]>self.rank[group_2]:
            self.group[group_2]=group_1
        elif self.rank[group_1]<self.rank[group_2]:
            self.group[group_1]=group_2
        else:
            self.group[group_1] = group_2
            self.rank[group_2]+=1
        return True

class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        ordered_edges = []
        #add the virtual vertex (index with 0) along with the new edges
        for index, weight in enumerate(wells):
            ordered_edges.append((weight,0,index+1))

        #add the existing edges
        for house_1,house_2, weight in pipes:
            ordered_edges.append((weight, house_1, house_2))

        #sort the entire edges by their weights
        ordered_edges.sort(key=lambda x: x[0])

        #iterate through the ordered edges
        uf = UnionFind(n)
        total_cost=0
        for cost, house_1, house_2 in ordered_edges:
            #determine if we should add the new edge to the final MST
            if uf.union(house_1,house_2):
                total_cost+=cost
        return total_cost