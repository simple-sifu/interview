# You are given a string s consisting of the following 
# characters: '(', ')', '{', '}', '[' and ']'.
#
# The input string s is valid if and only if:
#   1.Every open bracket is closed by the same type of close bracket.
#   2.Open brackets are closed in the correct order.
#   3.Every close bracket has a corresponding open bracket of the same type.
# 
# Return true if s is a valid string, and false otherwise.


class Solution:

    def validParenthesis(self, s:str) -> bool:

        stack = []
        closeToOpen = {
            "]":"[",
            ")":"(",
            "}": "{"
        }

        for char in s:
            if char in closeToOpen:
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False


sol = Solution()
inputStr = "()"
print("sol.validParenthesis(()) =", sol.validParenthesis(inputStr))
# output: True

inputStr = "()[]{}"
print("sol.validParenthesis(()) =", sol.validParenthesis(inputStr))
# output: True

inputStr = "()[{}"
print("sol.validParenthesis(()) =", sol.validParenthesis(inputStr))
# output: False

inputStr = "([)]"
print("sol.validParenthesis(()) =", sol.validParenthesis(inputStr))
# output: False                                     