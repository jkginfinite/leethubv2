class Solution:
    def countVowelStrings(self, n: int) -> int:
        vowels = list('aeiou')

        def recursive(L,count,n):
            LL=[]
            for i in L:
                for j in vowels:
                    if i[-1]<=j:
                        LL.append(i+j)
            if count<n:
                return recursive(LL,count+1,n)
            return len(LL)
        count=0
        if n==1:
            return len(vowels)
        return recursive(vowels,count,n-2)
    