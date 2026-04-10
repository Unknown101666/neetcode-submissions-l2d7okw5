class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] #list
        closetoopen = {")" : "(" , "]" : "[" , "}" : "{"} # mapping in the hash map
        for c in s:#traversing the string
            if c in closetoopen:#is the element in the map
                if stack and stack[-1] == closetoopen[c]: #does the TOS match the hashvalue of it's corresponding string, stack must not be empty, tos must match the hash key
                    stack.pop() # example '[]' will pop
                else:
                    return False # [) returns false
            else:
                stack.append(c)#adds element from string to stack
        return True if not stack else False 