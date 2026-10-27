# Prerequisites
# Before attempting this problem, you should be comfortable with:

# Two Pointers - Using pointers from both ends of a string to compare characters efficiently
# String Manipulation - Filtering characters, converting case, and reversing strings
# Character Classification - Identifying alphanumeric vs non-alphanumeric characters


# Problem
# Given a string s, return true if it is a palindrome, otherwise return false.
# A palindrome is a string that reads the same forward and backward. 
# It is also case-insensitive and ignores all non-alphanumeric characters.


# Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

# Input: s = "Was it a car or a cat I saw?"
# Output: true

# Input: s = "tab a cat"
# Output: false


class Solution:
    def isPalindrome(self, word: str):
        result = ''
        for char in word:
            if char.isalnum():
                result += char.lower()
        print("result =", result)
        return result == result[::-1]
        




sol = Solution()
print(sol.isPalindrome("Was it a car or a cat I saw?"))  # True

print(sol.isPalindrome("tab a cat")) 