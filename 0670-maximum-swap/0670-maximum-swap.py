class Solution:
    def maximumSwap(self, num: int) -> int:
        #conver the integer num to a string numStr to fasciilitate digit manipulation
        #get the length n of numStr
        #initialaize an array lastSeen of size 10 filled with -1 to store the last occurrence index of each digit
        #record the last occurrence of each digit
        #for eac index i in numStr, update lastSeen[numStr[i]-'0'] to i which stores the last position of each digit
        #traverse the digits numStr to find the dirst digit that casn be swapped with a larger one
        #for each index i, iterate d from 9 down to numstr[i]-'0'
        #if lastSeen[d]>i it means there exists a larger digit d that can be swapped with numStr[i]
        #perform the swap between numStr[i] and numStr[lastSeen[d]]
        #immediately retur the integer value of the modifed string using stoi(number)
        num_str = str(num)
        n = len(num_str)
        last_seen = [-1]*10

        for i in range(n):
            last_seen[int(num_str[i])]=i

        for i in range(n):
            for d in range(9, int(num_str[i]),-1):
                if last_seen[d]>i:
                    num_str = list(num_str)
                    num_str[i], num_str[last_seen[d]] = num_str[last_seen[d]], num_str[i]
                    num_str = "".join(num_str)
                    return int(num_str)
        return num