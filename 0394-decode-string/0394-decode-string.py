class Solution:
    def decodeString(self, s: str) -> str:
        # 1. keep adding to stack until we see a closing backet ]
        # 2. If we see a closing bracket pop stack until we see a opening bracket
        # 3. Pop the opening bracket, get the number to be multiplied, use while loop since number can be multi digit
        # 4. Multiply the string the extracted number and append back to the stack in case of nested brackets. Continue until the end of the string
        # 5. Join all elements of the stack list
        stack = []

        for char in s:
            if char!=']':
                stack.append(char)

            else:
                curr_str = ""
                while stack[-1]!='[':
                    curr_str = stack.pop()+curr_str
                stack.pop()

                curr_num = ''
                while stack and stack[-1].isdigit():
                    curr_num = stack.pop()+curr_num
                
                curr_str = int(curr_num)*curr_str
                stack.append(curr_str)
        return ''.join(stack)