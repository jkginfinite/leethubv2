class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000}
        
        number = 0
        stack = list(s)
        while stack:
            letter = stack.pop()
            if stack and letter in ["V","X","L","C","D","M"] and stack[-1]+letter in ["IV","IX","XL","XC","CD","CM"]:
                    next_letter=stack.pop()
                    value = d[letter] - d[next_letter]
                    print(value)
                    number+=value
                    
            else:
                value = d[letter]
                print(value)
                number+=value
        return number
            
            
        #III
        #I n+=1
        #I n+=1
        #I n+=1
        
        #LVIII
        #I n+=1
        #I n+=1
        #I n+=1
        #V n+=5
        #L n+=50
        
        #MCMXCIV
        #V n+=5
        #I and last==V n-=1
        #C n+=100
        #X n-=100
        #M n+=1000
        