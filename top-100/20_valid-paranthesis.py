class Solution:
    def isValid(self, s: str) -> bool:

        n=len(s)
        if n%2==1:
            return False

        matching_symbols={
            ')':'(',
            ']':'[',
            '}':'{'
        }

        stack = []

        for i in s:
            if i in matching_symbols:
                top=stack.pop() if stack else '#'
                if matching_symbols[i]!=top:
                    return False
            else:
                stack.append(i)
        return not stack
        

    

        