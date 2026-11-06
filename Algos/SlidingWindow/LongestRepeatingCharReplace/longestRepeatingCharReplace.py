# You are given a string s consisting of only uppercase english characters and an integer k. 
# You can choose up to k characters of the string and replace them with any other uppercase English character.
# After performing at most k replacements, return the length of the longest substring which 
# contains only one distinct character.

from collections import defaultdict

class Solution:

    def findLongestRepeating(self, s:str, k:int) -> int:
        result = 0
        l = 0
        count = defaultdict(int)
        for r in range(len(s)):
            count[s[r]] += 1

            if len(s[l:r+1]) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            result = len(s[l:r+1])
        return result



# Input: 
sol = Solution()
s = "ABABBA"
k = 2
print(sol.findLongestRepeating(s, k))
# Output: 5


# Input: 
sol = Solution()
s = "XYYX"
k = 2
print(sol.findLongestRepeating(s, k))
# Output: 4

# Input: 
sol = Solution()
s = "AAABABB"
k = 1
print(sol.findLongestRepeating(s, k))
# Output: 5