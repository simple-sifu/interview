def maxConsecutiveOnes(nums: list[int]) -> int:
    result = 0
    count = 0
    for num in nums:
        count =  count + 1 if num == 1 else 0 
        result = max(count, result)
    return result


print("maxConsecutiveOnes1: ", maxConsecutiveOnes([1,1,3,1,1,1,4,1,1,1,1,1]) )

print("maxConsecutiveOnes2: ", maxConsecutiveOnes([1,1,1,1, 3,1,1, 1,4,1,1]) )  

print("maxConsecutiveOnes2: ", maxConsecutiveOnes([1, 3,1,1, 1,4,1,1]) ) 