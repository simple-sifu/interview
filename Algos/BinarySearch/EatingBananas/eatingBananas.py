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

        while l <= r:
            
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







sol = Solution()
piles = [3,6,7,11]
h=8
# print("sol.minEatingSpeed()=", sol.minEatingSpeed(piles, h))
# output: 4


piles=[873375536,395271806,617254718,970525912,634754347,824202576,694181619,20191396,886462834,442389139,572655464,438946009,791566709,776244944,694340852,419438893,784015530,588954527,282060288,269101141,499386849,846936808,92389214,385055341,56742915,803341674,837907634,728867715,20958651,167651719,345626668,701905050,932332403,572486583,603363649,967330688,484233747,859566856,446838995,375409782,220949961,72860128,998899684,615754807,383344277,36322529,154308670,335291837,927055440,28020467,558059248,999492426,991026255,30205761,884639109,61689648,742973721,395173120,38459914,705636911,30019578,968014413,126489328,738983100,793184186,871576545,768870427,955396670,328003949,786890382,450361695,994581348,158169007,309034664,388541713,142633427,390169457,161995664,906356894,379954831,448138536]
h=943223529
print("sol.minEatingSpeed()=", sol.minEatingSpeed(piles, h))
# output: 46

piles = [1,4,3,2]
h = 9
# print("sol.minEatingSpeed()=", sol.minEatingSpeed(piles, h))
# output: 2


piles = [25,10,23,4]
h = 4
# print("sol.minEatingSpeed()=", sol.minEatingSpeed(piles, h))
# output: 25