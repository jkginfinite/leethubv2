class Solution:
    def kthCharacter(self, k: int) -> str:
        alphabet = list('abcdefghijklmnopqrstuvwxyz')
        word = alphabet[0]
        def recursive(word,k):
            if len(word)>=k:
                return word[k-1]
            new = ''
            for i in word:
                index = alphabet.index(i)
                if index+1<26:
                    next_char = alphabet[index+1]
                else:
                    next_char = alphabet[(26%index)+1]
                new+=next_char
            word+=new
            return recursive(word,k)
        return recursive(word,k)