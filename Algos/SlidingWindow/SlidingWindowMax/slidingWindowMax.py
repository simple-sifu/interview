# You are given an array of integers nums and an integer k. 
# There is a sliding window of size k that starts at the left edge of the array. 
# The window slides one position to the right until it reaches the right edge of the array.

# Return a list that contains the maximum element in the window at each step.

import collections

class Solution:
    def maxSlidingWindow(self, nums: [int], k: int) -> []:
        output = []
        q = collections.deque()
        l = r = 0

        for r in range(len(nums)):

            # pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove left val from window
            if l > q[0]:
                q.popleft()

            # dont add until r has reached
            # full k window.
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output


sol = Solution()
nums = [1,2,1,0,4,2,6]
k = 3
# Output: [2,2,4,4,6]
# print(sol.maxSlidingWindow(nums, k))

nums = [8, 7, 6, 9]
k = 2
# Output: [2,2,4,4,6]
print(sol.maxSlidingWindow(nums, k))