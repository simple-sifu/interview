# You are given an array of integers nums and an integer k. 
# There is a sliding window of size k that starts at the left edge of the array. 
# The window slides one position to the right until it reaches the right edge of the array.

# Return a list that contains the maximum element in the window at each step.

import collections

class Solution:
    def maxSlidingWindow(self, nums: [int], k: int) -> []:
        output = []
        q = collections.deque() # store indices only
        lptr = 0
        for rptr in range(len(nums)):

            
            print("loop: rptr=", rptr, ", nums[rptr] =", nums[rptr])
            if q: 
                print(", nums[q[-1]]=", nums[q[-1]])
            # remove smaller numbers
            while q and nums[q[-1]] < nums[rptr]:
                print(">>>> q.pop() nums[q[-1]]=", nums[q[-1]])
                q.pop()
            q.append(rptr)

            # remove items left of window
            if lptr > q[0]:
                q.popleft()
            print("q =", q)

            # wait until window is k items
            if (rptr + 1) >= k:
                output.append(nums[q[0]])
                lptr += 1

            print("**** output =", output, "\n\n")
        return output


sol = Solution()
nums = [1,2,1,0,4,2,6]
k = 3
# Output: [2,2,4,4,6]
print(sol.maxSlidingWindow(nums, k))