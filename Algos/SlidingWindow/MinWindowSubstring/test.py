class Solution:

    def minWindow(self, s:str, tsubstring:str) -> str:
        
        substringHash, windowHash = {}, {}

        for t in tsubstring:
            substringHash[t] = 1 + substringHash.get(t, 0)

        have = 0
        need = len(tsubstring)
        leftPtr = 0
        result = [-1, -1]
        resultLen = float("infinity")
        for rightPtr in range(len(s)):
            print("loop: rightPtr =", rightPtr, ", have =", have)
            key = s[rightPtr]

            if key in substringHash:
                windowHash[key] = 1 + windowHash.get(key, 0)

            print("key =", key, ", substringHash =", substringHash, ", windowHash=", windowHash, ", s=", s)
            if key in substringHash and substringHash[s[rightPtr]] == windowHash[s[rightPtr]]:
                have += 1
            
            print("before while: have =", have)

            while have == need:

                print("[s[leftPtr] =", s[leftPtr], ", leftPtr =", leftPtr,", s=", s)

                print("***** While: windowHash =", windowHash, "[s[leftPtr] =", s[leftPtr])

                if (rightPtr - leftPtr + 1) < resultLen:
                    resultLen = rightPtr - leftPtr + 1
                    result = [leftPtr, rightPtr]

                if s[leftPtr] in substringHash:
                    windowHash[s[leftPtr]] -= 1

                if s[leftPtr] in substringHash and windowHash[s[leftPtr]] < substringHash[s[leftPtr]]:
                    have -= 1

                leftPtr += 1

                print("windowHash =", windowHash, ", leftPtr =", leftPtr, "s[leftPtr] =", s[leftPtr], ", have=", have, ", resultLen=", resultLen)
            
        l,r = result
        print ("result =", result, ", l=", l, ", r=", r)
        
        return s[l:r+1] if resultLen != float("infinity") else ""


sol = Solution()
s = "ADOBECODEBANC"
t = "ABC"
print("sol.minWindow() =", sol.minWindow(s,t))