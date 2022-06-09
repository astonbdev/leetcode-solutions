class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        close_brackets = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        stack = []

        # print("stack", stack)

        for char in s:
            # print("char", char)
            # print("stack", stack)

            if char in open_brackets:
                stack.insert(0,char)
            elif len(stack) == 0:
                return False
            elif close_brackets[char] == stack[0]:
                stack.pop(0)
            else:
                return False

        if len(stack) > 0:
            return False

        return True
