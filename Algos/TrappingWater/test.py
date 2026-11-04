# You are given an array of non-negative integers height which represent an elevation map. 
# Each value height[i] represents the height of a bar, which has a width of 1.


class Solution:

    def trapWater(self, heights: list[int]) -> int:
        l, r = 0, len(heights) - 1
        waterAmount = 0
        maxLeft, maxRight = heights[l], heights[r]

        while l < r:
            if maxLeft <= maxRight:
                l += 1
                maxLeft = max(maxLeft, heights[l])
                waterAmount += maxLeft - heights[l]
                print("leftSide: l =", l, ", r =", r, ", left height =", heights[l],  ", waterAmount =", waterAmount, ", maxLeft =", maxLeft, "maxRight =", maxRight)

            else:
                r -= 1
                maxRight = max(maxRight, heights[r])
                waterAmount += maxRight - heights[r]
                print("rightSide: l =", l, ", r =", r, ", right height =", heights[r],  ", waterAmount =", waterAmount, ", maxLeft =", maxLeft, "maxRight =", maxRight)



        return waterAmount






sol = Solution()
heights = [0,1,0,2,1,0,1,3,2,1,2,1]
print(sol.trapWater(heights)) 
# 6

heights = [0,2,0,3,1,0,1,3,2,1]
print(sol.trapWater(heights)) 
# 9