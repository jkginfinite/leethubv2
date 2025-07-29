class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals)==1:
            return True

        #L = []
        #for index in range(len(intervals)):
        #    L.append(intervals[index][0])
        
        #L.sort()
        #L = [[i] for i in ]
        intervals.sort()
        for index in range(1,len(intervals)):
            if intervals[index][0]<intervals[index-1][-1]:
                return False
        return True