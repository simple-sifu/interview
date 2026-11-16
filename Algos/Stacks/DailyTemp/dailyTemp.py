# You are given an array of integers temperatures where temperatures[i] represents the daily temperatures 
# on the ith day.

# Return an array result where result[i] is the number of days after the ith day before a warmer 
# temperature appears on a future day. If there is no day in the future where a warmer temperature 
# will appear for the ith day, set result[i] to 0 instead.


class Solution:

    def dailyTemp(self, temperatures: list[int]) -> [int]:
        result = [0] * len(temperatures)
        stack = [] # temp, index
        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                t, stackIndex = stack.pop()
                result[stackIndex] = index - stackIndex
            stack.append([temp, index])
        return result 



sol = Solution()
# Input: 
temperatures = [30,38,30,36,35,40,28]
print ("daily Temperatures =", sol.dailyTemp(temperatures))
# Output: [1,4,1,2,1,0,0]


# Input: 
temperatures = [22,21,20]
print ("daily Temperatures =", sol.dailyTemp(temperatures))
# Output: [0,0,0]