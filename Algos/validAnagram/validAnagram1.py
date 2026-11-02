# Given two strings s and t, return true if the two strings are anagrams of each other, 
# otherwise return false. Two strings are anagrams if they contain the same characters, 
# with each character appearing the same number of times, regardless of order.


# Example 1:
# Input: s = "racecar", t = "carrace"
# Output: true

# Example 2:
# Input: s = "jar", t = "jam"
# Output: false

# Example 3:
# Input: s = "x", t = "x"
# Output: true

# Constraints:
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.

def isAnagram(word: str, secondWord: str) -> bool:
    countDict = {}
    for c in word:
        if c in countDict:
            countDict[c] += 1
        else:
            countDict[c] = 1
    for c in secondWord:
        if (c in countDict) and (countDict[c] != 0):
            countDict[c] -= 1
        else:
            return False
    count = 0
    for value in countDict.values():
        count += value 
    return True if count == 0 else False

            
s="racecar"
t="carrace"
print(f'is this an Anagram ? {isAnagram(s,t)} for {s} and {t}')

s = "jar"
t = "jam"
print(f'is this an Anagram ? {isAnagram(s,t)} for {s} and {t}')


s = "x"
t = "x"
print(f'is this an Anagram ? {isAnagram(s,t)} for {s} and {t}')
