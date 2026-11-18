# You are given an m x n 2-D integer array matrix and an integer target.

# Each row in matrix is sorted in non-decreasing order.
# The first integer of every row is greater than the last integer 
# of the previous row.

# Return true if target exists within matrix or false otherwise.

class Solution:
    def twoDegreeMatrix(self, matrix: [[int]], int) -> bool:
        topRow, bottomRow = 0, len(matrix) - 1

        while topRow <= bottomRow:
            middleRow = (topRow + bottomRow) // 2
            print("middleRow =", middleRow, ", matrix[middleRow][-1]=", matrix[middleRow][-1])
            if matrix[middleRow][-1] < target:
                print("topRow... target=", target)
                topRow = middleRow + 1
            elif matrix[middleRow][0] > target:
                print("bottomRow... target=", target)
                bottomRow = middleRow - 1
            break

        print("topRow =", topRow, ", bottomRow =", bottomRow)
        if not (topRow <= bottomRow):
            return False
        
        middleRow = (topRow + bottomRow) // 2
        print("middleRow =", middleRow)
        leftColumn, rightColumn = 0, len(matrix[0])- 1
        while leftColumn <= rightColumn:
            middleColumn = (leftColumn + rightColumn)//2
            print("middleColumn=", middleColumn, ", matrix[middleRow][middleColumn]=", matrix[middleRow][middleColumn])
            if target < matrix[middleRow][middleColumn]:
                rightColumn = middleColumn - 1
            elif target > matrix[middleRow][middleColumn]:
                leftColumn = middleColumn + 1
            else:
                return True
        return False

                 


sol = Solution()
matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
target = 10
print("sol.twoDegreeMatrix()=", sol.twoDegreeMatrix(matrix, target))
# Output: true