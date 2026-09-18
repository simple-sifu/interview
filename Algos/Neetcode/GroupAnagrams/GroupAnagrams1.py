from collections import defaultdict

# Given an array of strings strs, group all anagrams together into sublists. 
# You may return the output in any order.
# An anagram is a string that contains the exact same characters as 
# another string, but the order of the characters can be different.


# Example 1:
# Input: strs = ["act","pots","tops","cat","stop","hat"]
# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

# Example 2:


# Example 3:


# Constraints:
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.

def groupAnagrams(s:( list[str])) -> bool:
    res = defaultdict(list)
    for s in strs:
        count = [0] * 26 # a ... z

        for code in s:
            count[ord(code) - ord("a")] += 1

        res[tuple(count)].append(s)

    return res.values()


            
strs = ["act","pots","tops","cat","stop","hat"]
print('Group Anagrams for %s', groupAnagrams(strs))
# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]