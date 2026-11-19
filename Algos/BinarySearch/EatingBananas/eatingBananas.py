# You are given an integer array piles where piles[i] is the number of bananas in the ith pile. 
# You are also given an integer h, which represents the number of hours you have to eat all the bananas.

# You may decide your bananas-per-hour eating rate of k. Each hour, you may choose a pile of bananas 
# and eats k bananas from that pile. If the pile has less than k bananas, you may finish eating the pile 
# but you can not eat from another pile in the same hour.

# Return the minimum integer k such that you can eat all the bananas within h hours.

import math
class Solution:

    def minEatingSpeed(self, piles:list[int], h:int) -> int:
        # setup l and r pointers to go from 1 to largest number
        l, r = 1, max(piles)
        result = r

        while l < r:
            # find midpt between l & right
            midpt = (l + r)//2
            # add up hours for that midpoint
            hours = 0
            for p in piles:
                hours += math.ceil(p/midpt)
            # compare hours to max hours
            if hours <= h:
                result = min(midpt, result)
                r = midpt - 1
            else:
                l = midpt + 1
        return result
        pass







sol = Solution()
piles = [3,6,7,11]
h=8
print("sol.minEatingSpeed()=", sol.minEatingSpeed(piles, h))
# output: 4


piles = [1,4,3,2]
h = 9
print("sol.minEatingSpeed()=", sol.minEatingSpeed(piles, h))
# output: 2


piles = [25,10,23,4]
h = 4
print("sol.minEatingSpeed()=", sol.minEatingSpeed(piles, h))
# output: 25