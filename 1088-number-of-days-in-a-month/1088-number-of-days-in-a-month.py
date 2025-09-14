class Solution:
    def numberOfDays(self, year: int, month: int) -> int:
        days_in_months = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
        if (year%4==0 and year%100!=0) or (year%400==0):
            days_in_months[2]=29
        return days_in_months[month]