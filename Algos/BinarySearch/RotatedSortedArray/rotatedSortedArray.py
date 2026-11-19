# Find Minimum in Rotated Sorted Array

# You are given an array of length n which was originally sorted in ascending order. 
# It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] 
# might become:

# [3,4,5,6,1,2] if it was rotated 4 times.
# [1,2,3,4,5,6] if it was rotated 6 times.
# Notice that rotating the array 4 times moves the last four elements 
# of the array to the beginning. Rotating the array 6 times produces the original array.

# Assuming all elements in the rotated sorted array nums are unique, 
# return the minimum element of this array.

# A solution that runs in O(n) time is trivial, can you write an algorithm 
# that runs in O(log n) time?

class Solution:
    def findMin(self, nums: list[int]) -> int:
        # default result to first item in array
        l, r = 0, len(nums) - 1
        result = nums[0]
        while l <= r:
            # if subarray is sorted then just take 
            # the min
            if nums[l] < nums[r]:
                result = min(result, nums[l])
                break;

            # binary search
            midpoint = (l+r)//2
            result = min(result, nums[midpoint])
            print("midpoint =", midpoint, ", result =", result)
            print("nums[midpoint] =", nums[midpoint], ", nums[l] =", nums[l])
            if nums[midpoint] >= nums[l]:
                # search left
                l = midpoint + 1
            else:
                # search right
                r = midpoint - 1
        return result
            



sol = Solution()
nums = [3,4,5,6,1,2]
print("sol.findMin(nums) =", sol.findMin(nums))
# output 1


nums = [4,5,0,1,2,3]
# print("sol.findMin(nums) =", sol.findMin(nums))
# output 0


nums = [4,5,6,7]
# print("sol.findMin(nums) =", sol.findMin(nums))
# output 4


