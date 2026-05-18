class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {
                       ")":"(",
                       "}":"{",
                       "]":"["
                       }

        for c in s:
            if c not in closeToOpen:
                stack.append(c)
            else:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False

        return True if not stack else False 

        # stack = []
        # map = {
        #     ")":"(",
        #     "]":"[",
        #     "}":"{"
        # }

        # for val in s:
        #     if val not in map:
        #         stack.append(val)
        #     else:
        #         if stack and stack[-1]==map[val]:
        #             stack.pop()
        #         else:
        #             return False 
        # return True if not stack else False

        








































        stack = []
        map = {
            "]":"[",
            "}":"{",
            ")":"("
        }
        for char in s:
            if char not in map:
                stack.append(char)
            else:
                if stack and map[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False

          
        