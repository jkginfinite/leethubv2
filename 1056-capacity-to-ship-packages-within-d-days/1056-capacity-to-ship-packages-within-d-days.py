class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        maxWeight, totalWeight = -1, 0

        for weight in weights:
            maxWeight = max(maxWeight, weight)
            totalWeight+=weight
            
        while maxWeight<totalWeight:
            mid = (maxWeight+totalWeight)//2
            daysNeeded, currWeight = 1,0
            for weight in weights:
                if currWeight+weight>mid:
                    daysNeeded+=1
                    currWeight=0
                currWeight+=weight
            if daysNeeded>days:
                maxWeight=mid+1
            else:
                totalWeight=mid
        return maxWeight
            




        