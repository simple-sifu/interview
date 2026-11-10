class Solution:

    def foundPermutation(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1count, s2count = [0] * 26, [0] * 26
        # compute counts for both counts
        for l in range(len(s1)):
            s1index = ord(s1[l]) - ord("a")
            s2index = ord(s2[l]) - ord("a")
            s1count[s1index] += 1
            s2count[s2index] += 1

        print("s1count =", s1count)
        print("s2count =", s2count)

        matches = 0
        # calculate matches for both counts
        for i in range(26):
            if s1count[i] == s2count[i]:
                matches += 1

        print("matches =", matches)
        # sliding window with lptr and Rptr
        # compare both s1 and s2
        lptr = 0
        for rptr in range(len(s1), len(s2)):
            if matches == 26: return True

            index = ord(s2[rptr]) - ord("a")
            s2count[index] += 1
            if s1count[index] == s2count[index]:
                matches += 1
            elif s1count[index] + 1 == s2count[index]:
                matches -= 1


            index = ord(s2[lptr]) - ord("a")
            s2count[index] -= 1
            if s1count[index] == s2count[index]:
                matches += 1
            elif s1count[index] - 1 == s2count[index]:
                matches -= 1
            lptr += 1

        return matches == 26

sol = Solution()
s1 = "abc"
s2 = "xyxabc"
print(sol.foundPermutation(s1, s2))

s1 = "ab"
s2 = "eidbaoooo"
# print(sol.foundPermutation(s1, s2))
# output True


s1 = "ab"
s2 = "eidbooooo"
# print(sol.foundPermutation(s1, s2))
# output False