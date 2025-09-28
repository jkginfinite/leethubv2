class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        #find all contiguous substrings
        #find the ones which only consist of vowels
        vowels = 'aeiou'
        non_vowels = [j for j in 'abcdefghijklmnopqrstuvwxyz' if j not in vowels]
        substrings = []

        WORD = list(word)
        count = 0
        for i in range(len(word)):
            for j in range(i+1,len(word)+1):
                window = WORD[i:j]
                if not any([n in window for n in non_vowels]) and all([v in window for v in vowels]):
                    count+=1
        return count