def longestConsecutive(nums: list[int]):
    numSet = set(nums)
    largestSequence = 0

    for num in numSet:
        if (num - 1) not in numSet:
            length = 1
            while (num + length) in numSet:
                length += 1
            largestSequence = max(length, largestSequence)

    return largestSequence


input = [2,20,4,10,3,4,5]
print("longestConsecutive = ", longestConsecutive(input))
# output = 4



input = [0,3,2,5,4,6,1,1]
print("longestConsecutive = ", longestConsecutive(input))
# output = 7