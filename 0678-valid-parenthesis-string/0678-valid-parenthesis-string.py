class Solution(object):
    def checkValidString(self, s: str) -> bool:
        #initialize two stacks: one for open brackers to store indices of open brackets
        #the other stack for the astericks to store indices of astericks
        #iterate through the strin s character by character
        #if the char = '(' push its index onto the openBrackets stack
        #if the char="*" push its index to the astericks stack
        #if the current char=")"
        #if openBrackets is not empty, pop an element from it (removing the matching open bracket)
        #if astericks is not empty pop an element from astericks
        #if neither an open bracket nor an asterick is available, return false
        #after iterating through the entire string, check if any remaining open brackets and astericks can balance each other
        #while both open brackets and astericks
        #if the top element of openBrackerts is greater than the top element of astericks it means the the open bracket appears after the astericks, which cannot be balanced, so return false
        #otherwise pop elements from both openBrackets and astericks stakcs
        #if after the above step, openBrackets it empty, it means all open brackets have been matched or balanced so return True. otherwise return false
        open_brackets = [] #store indices of open brackets and astericks
        astericks = []

        for i, ch in enumerate(s):
            #if current character is an open bracket, push its index onto the stack
            if ch=="(":
                open_brackets.append(i)
            #if current character is an astericks, push its index onto the stack
            elif ch=="*":
                astericks.append(i)
            else:
                if open_brackets: #there are open brackets avaialble, use them to balance the closing bracket
                    open_brackets.pop()
                elif astericks: #if no open brackets are avaialble, use an asterick to balance the closing bracket
                    astericks.pop()
                else: #unmatched ) and no '*' to balance it
                    return False

        while open_brackets and astericks:
            if open_brackets.pop()>astericks.pop():
                return False #if an open bracker appears after an asterick, it cannot be balanced, return false
            #if all open brackets are matched and. there no no unmatched open brackets left, return true
        return not open_brackets
