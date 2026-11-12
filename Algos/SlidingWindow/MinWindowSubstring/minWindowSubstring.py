class Solution:

    def minWindow(self, s:str, tsubstring:str) -> str:
        if tsubstring == "" : return ""

        if len(tsubstring) > len(s): return ""

        thash, windowHash = {}, {}

        # setup thash substring I need to have.
        for letter in tsubstring:
            thash[letter] = 1 + thash.get(letter, 0)
        
        lptr = 0
        have, need = 0, len(thash)
        result, resultLen = [-1,-1], float("infinity")
        for rptr in range(len(s)):

            key = s[rptr]
            windowHash[key] = 1 + windowHash.get(key, 0)

            if key in thash and windowHash[key] == thash[key]:
                have += 1


            while have == need:
                # update our result
                if rptr-lptr+1 < resultLen:
                    result = [lptr, rptr]
                    resultLen = rptr - lptr +1

                # pop from the left of our window
                windowHash[s[lptr]] -= 1

                if s[lptr] in thash and windowHash[s[lptr]] < thash[lptr]:
                    have -= 1
                lptr += 1
 
        l, r = result
        # return minimum window of string
        return s[l:r+1] if resultLen != float("infinity") else ""



sol = Solution()
s = "ADOBECODEBANC"
t = "ABC"
print("sol.minWindow() =", sol.minWindow(s,t))