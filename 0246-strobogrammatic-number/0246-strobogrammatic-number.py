class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        rotated_string = ''

        for character in num[::-1]:
            if character in ['0','1','8']:
                rotated_string+=character
            elif character=='6':
                rotated_string+='9'
            elif character=='9':
                rotated_string+='6'
            else:
                return False
        return rotated_string==num