class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiou'
        given_vowels = {}
        given_letters = []

        num = 0
        for i in s:
            if i.lower() in vowels:
                _ = num
                given_vowels[_] = i
                num+=1
            else:
                _ = i
            given_letters.append(_)

        #print(given_vowels)
        u = dict(sorted(given_vowels.items(), key=lambda x: x[0],reverse=True))
        print(given_letters)
        print(u)
        n = 0
        d = {}
        for val in u.values():
            d[n] = val
            n+=1
        
        m = 0
        for index in range(len(given_letters)):
            _ = given_letters[index]
            if type(_)==int:
                given_letters[index]=d[m]
                m+=1
        print(given_letters)
        return ''.join(given_letters)
