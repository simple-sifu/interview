# Given an integer array nums and an integer k, return the k most 
# frequent elements within the array.
# The test cases are generated such that the answer is always unique.
# You may return the output in any order.

def topKFrequent(nums: list[int], k: int) -> list[int]:

    print( '*' * 20)
    counts = {}

    for num in nums:
        counts[num] = 1 + counts.get(num, 0) 

    freq = [[] for _ in range(len(nums) + 1)]
    for num, count in counts.items():
        freq[count].append(num)

    result = []
    for index in range(len(freq)-1, 0, -1):
        if len(result) >= k:
            break
        if freq[index]:
            result.append(freq[index][0])

    return result
        


    

# Ex 1
# Input: nums = [1,2,2,3,3,3,4], k = 2
# Output: [2,3]
print(topKFrequent([1,2,2,3,3,3,4], 2))


# Ex 2
# Input: nums = [7,7], k = 1
# Output: [7]
print(topKFrequent([7,7], 1))

# Constraints
# 1 <= nums.length <= 10^4.
# -1000 <= nums[i] <= 1000
# 1 <= k <= number of distinct elements in nums