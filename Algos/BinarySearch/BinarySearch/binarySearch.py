# You are given an array of distinct integers nums, sorted in ascending order, 
# and an integer target.

# Implement a function to search for target within nums. If it exists, then 
# return its index, otherwise, return -1.

# Your solution must run in O(log n)
# O(logn) time.


class Solution:

    def search(self, nums: [int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (right + left)//2
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                return middle
        return -1


sol = Solution()

nums = [-1,0,2,4,6,8]
target = 4
print("sol.search() =", sol.search(nums, target))
# Output: 3


nums = [-1,0,2,4,6,8]
target = 3
print("sol.search() =", sol.search(nums, target))
# Output: -1