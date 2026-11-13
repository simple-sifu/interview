# Design a stack class that supports the push, pop, top, 
# and getMin operations.

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.

# Each function should run in O(1) time.

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        minVal =  min(self.minStack[-1], val) if self.minStack else val
        self.minStack.append(minVal)
        print("push: stack =", self.stack, ", minStack =", self.minStack)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        print("pop: stack =", self.stack, ", minStack =", self.minStack)

    def top(self) -> int:
        print("top: top =", self.stack[-1])
        return self.stack[-1]

    def getMin(self) -> int:
        print("getMin: min =", self.minStack[-1])
        return self.minStack[-1]
        

# Input: ["MinStack", "push", 1, "push", 2, "push",
#          0, "getMin", "pop", "top", "getMin"]

# Output: [null,null,null,null,0,null,2,1]

# Explanation:
minStack = MinStack()
minStack.push(1)
minStack.push(2)
minStack.push(0)
minStack.getMin() # return 0
minStack.pop()
minStack.top()    # return 2
minStack.getMin() # return 1