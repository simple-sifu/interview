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
        
        l, r = 0, len(word) - 1
        while l < r:
            while l < r and not self.isAlphaNumeric(word[l]):
                l += 1
            while r > l and not self.isAlphaNumeric(word[r]):
                r -= 1
            if word[l].lower() != word[r].lower():
                return False
            l, r = l+1, r-1

        return True


    def isAlphaNumeric(self, letter: str) -> bool:
        return (ord(letter) >= ord("A") and ord(letter) <= ord("Z") or
                ord(letter) >= ord("a") and ord(letter) <= ord("z") or
                ord(letter) >= ord("0") and ord(letter) <= ord("9"))

                

        




sol = Solution()
print(sol.isPalindrome("Was it a car or a cat I saw?"))  # True

print(sol.isPalindrome("tab a cat")) 