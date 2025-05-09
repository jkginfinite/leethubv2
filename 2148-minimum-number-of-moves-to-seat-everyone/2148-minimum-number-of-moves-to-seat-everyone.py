class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        students = sorted(students)
        seats = sorted(seats)
        moves = 0
        for i in range(len(students)):
            moves+=abs(students[i]-seats[i])
        return moves
        