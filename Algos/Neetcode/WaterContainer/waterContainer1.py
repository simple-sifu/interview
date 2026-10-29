class Solution:
    def maxArea(self, heights: list[int]) -> int:
        l, r = 0, len(heights) - 1
        result = 0
        while (l<r):
            print("while loop: l=", l, ", r=", r)
            lowerHeight = min(heights[l], heights[r])
            area = lowerHeight * (r-l)
            print("area =", area, ", heights[l]=", heights[l], ", heights[r]=", heights[r])
            result = max(area, result)
            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        return result


sol = Solution()
heights = [1,7,2,5,4,7,3,6]
print(sol.maxArea(heights))
#36

heights = [1,8,6,2,5,4,8,3,7]
print(sol.maxArea(heights))
# 49