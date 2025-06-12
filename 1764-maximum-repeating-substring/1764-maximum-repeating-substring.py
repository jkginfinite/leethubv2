class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        if word not in sequence:
            return 0
        if sequence==word:
            return 1
        
        n=len(sequence)
        k=1
        while k<=n and k*word in sequence:
            k+=1
        return k-1