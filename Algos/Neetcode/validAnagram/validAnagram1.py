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

def isAnagram(s: str, t: str) -> bool:
    countDict = {}
    for schar in s:
        if schar in countDict:
            countDict[schar] += 1
        else:
            countDict[schar] = 1
    for tchar in t:
        if tchar in countDict:
            print("tchar =", tchar," and countDict[tchar] =", countDict[tchar])
        else:
            print("tchar =", tchar)
        if (tchar in countDict) and (countDict[tchar] != 0):
            countDict[tchar] -= 1
        elif tchar not in countDict or countDict[tchar] == 0:
            return False
    count = 0
    for value in countDict.values():
        count += value 
    return True if count == 0 else False

            
s="racecar"
t="carrace"
print('isAnagram = %b for %s and %s', isAnagram(s,t), s, t)

s = "jar"
t = "jam"
print('isAnagram = %b for %s and %s', isAnagram(s,t), s, t) 


s = "x"
t = "x"
print('isAnagram = %b for %s and %s', isAnagram(s,t), s, t)  
