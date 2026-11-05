# You are given an array of non-negative integers height which represent an elevation map. 
# Each value height[i] represents the height of a bar, which has a width of 1.


class Solution:

    def trapWater(self, heights: list[int]) -> int:


        l, r = 0, len(heights) - 1
        maxLeft, maxRight = heights[l], heights[r]
        waterTrappedAmount = 0

        while l<r:
            if maxLeft <= maxRight:
                l += 1
                maxLeft = max(maxLeft, heights[l])
                waterTrappedAmount += maxLeft - heights[l]

            else:
                r -= 1
                maxRight = max(maxRight, heights[r])
                waterTrappedAmount += maxRight - heights[r]

        return waterTrappedAmount



sol = Solution()
heights = [0,1,0,2,1,0,1,3,2,1,2,1]
print(sol.trapWater(heights)) 
# 6

heights = [0,2,0,3,1,0,1,3,2,1]
print(sol.trapWater(heights)) 
# 9