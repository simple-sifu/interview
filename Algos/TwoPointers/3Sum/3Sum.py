# Given an integer array nums, return all the triplets 
# [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, 
# and the indices i, j and k are all distinct.

# The output should not contain any duplicate triplets. You may 
# return the output and the triplets in any order.


# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]


class Solution:
    def threeSum(self, nums: list[int]) -> list[int]:

        nums.sort()
        result = []
        l, r = 0, len(nums) - 1
        for i, target in enumerate(nums):
            print("loop 0: i =", i, ", target=", target)
            if i > 0 and target == nums[i-1]:
                continue

            l, r = i+1, len(nums) - 1
            while l < r:
                print("loop 1: l =", l, ", r=", r)
                threeSum = target + nums[l] + nums[r]
                if threeSum > 0:
                    print("gtr than 0")
                    r -= 1
                elif threeSum < 0:
                    print("less than 0")
                    l += 1
                else:
                    print("equal 0")
                    result.append([target, nums[l], nums[r]])
                    l +=1
                    while nums[l] == nums[l-1] and l<r:
                        l += 1
            print("**** end loop *****\n")
        return result




sol = Solution()
nums=[-3, 0, -3, 2, 4, 1]
print(sol.threeSum(nums))

nums=[-1,0,1,2,-1,-4]
print(sol.threeSum(nums))