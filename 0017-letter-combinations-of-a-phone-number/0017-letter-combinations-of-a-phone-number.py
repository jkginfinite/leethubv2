from itertools import combinations
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }   
        #use backtracking function to generate all possible combinations
        #the function should take 2 primary inputs: the current combination of letters we have, path and the index we are currently checking
        #as a base case, if our current combinations of letters is the same input as our digits, that means we have a complete combination, therefore add it to our answer and backtrack
        #otherwise get all the letters that correspond with the current digit we are looking at, digits[index]
        #loop through these letters. for each letter, add the letter to our current path and call backtrack again, but move on the next digit by incrementing index by 1
        #make sure to remove the letter from path once finished with it

        def backtrack(index,path):
            #if the path is the same legnth as digits, we have a complete combination
            if len(path)==len(digits):
                combinations.append("".join(path))
                return
            
            #get the letters that the current digit maps to, and loop through them
            possible_letters = letters[digits[index]]
            for letter in possible_letters:
                #add the letter to our current path
                path.append(letter)
                #move onto the next digit
                backtrack(index+1,path)
                #backtrack by removing the letter before moving onto the next
                path.pop()
        
        #initiate backtracking with an empty path and starting index of 0
        combinations = []
        path = []
        backtrack(0,path)
        return combinations


        