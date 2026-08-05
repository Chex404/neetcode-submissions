class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        stack.append(s[0])

        for ch in s[1:]:

            if not stack:
                stack.append(ch)

            elif (stack[-1] == '(' and ch == ')') or (stack[-1] == '{' and ch == '}') or (stack[-1] == '[' and ch == ']'):
                stack.pop()

            else:
                stack.append(ch)

        if not stack:
            return True
        else:
            return False

            
        