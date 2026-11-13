# Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without duplicate characters.
# A substring is a contiguous sequence of characters within a string.



class Solution:

    def findUniqueString(self, string: str):
        l = 0
        size = 0
        result = set()
        for r in range(len(string)):
            while string[r] in result:
                result.remove(string[l])
                l += 1
            result.add(string[r])
            size = max(size, r - l + 1)
        return size


# Example 1:
# Input: 
s = "abcabcbb"
sol = Solution()
print(sol.findUniqueString(s))
# output 3

# Example 2:
# Input: 
s = "zxyzxyz"
sol = Solution()
print(sol.findUniqueString(s))
# Output: 3

# Example 3:
# Input: 
s = "xxxx"
sol = Solution()
print(sol.findUniqueString(s))
# Output: 1