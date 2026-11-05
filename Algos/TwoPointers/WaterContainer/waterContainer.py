class Solution:
    def maxArea(self, heights: list[int]) -> int:
        result = 0
        for l in range(len(heights)):
            print("loop l: l =", l)
            for r in range(len(heights) - 1, l+1, -1):
                print("loop r: r =", r)
                lowerHeight = min(heights[r], heights[l])
                area = lowerHeight * (r-l)
                print("area =", area, ", lowerHeight =", lowerHeight, ", r-l =", r-l)
                result = max(area, result)
        print("\n *********************")
        return result


sol = Solution()
heights = [1,7,2,5,4,7,3,6]
print(sol.maxArea(heights))
#36

heights = [1,8,6,2,5,4,8,3,7]
print(sol.maxArea(heights))
# 49