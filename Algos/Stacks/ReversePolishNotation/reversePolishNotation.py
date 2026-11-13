# You are given an array of strings tokens that represents a valid 
# arithmetic expression in Reverse Polish Notation.
# Return the integer that represents the evaluation of the expression.

# The operands may be integers or the results of other operations.
# The operators include '+', '-', '*', and '/'.
# Assume that division between integers always truncates toward zero.


# Input: 
tokens = ["1","2","+","3","*","4","-"]

class PolishCalculator:

    def compute(self, tokens: list[str]) -> int:

        stack = []

        for token in tokens:
            print("loop: token =", token)
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                b, a = stack.pop(), stack.pop()
                stack.append(int(a/b))
            else:
                stack.append(int(token))
            print("stack =", stack)
        return stack[-1]






polishCalculator = PolishCalculator()

# Input: 
tokens = ["1","2","+","3","*","4","-"]
print("polishCalculator: ",polishCalculator.compute(tokens))

# Output: 5
# Explanation: ((1 + 2) * 3) - 4 = 5

