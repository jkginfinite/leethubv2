class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        operator = "+"

        for index, char in enumerate(s):
            if char.isdigit():
                num = num*10+int(char)
            
            if char in "+-*/" or index==len(s)-1:
                if operator=="+":
                    stack.append(num)
                elif operator=="-":
                    stack.append(-num)
                elif operator=="*":
                    stack.append(stack.pop()*num)
                elif operator=='/':
                    last = stack.pop()
                    if last<0:
                        stack.append(-(-last//num))
                    else:
                        stack.append(last//num)
                operator=char
                num=0
        return sum(stack)      

