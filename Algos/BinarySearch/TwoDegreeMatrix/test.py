# You are given an m x n 2-D integer array matrix and an integer target.

# Each row in matrix is sorted in non-decreasing order.
# The first integer of every row is greater than the last integer 
# of the previous row.

# Return true if target exists within matrix or false otherwise.

class Solution:
    def twoDegreeMatrix(self, matrix: [[int]], target: int) -> bool:
        # dealing with matrix of 2 arrays
        # matrix[][] - row, column
        # 0, len(matrix) -1
        topRow, bottomRow = 0, len(matrix) - 1


        # while loop to find middle row between top and bottom rows
        while topRow <= bottomRow:
            middleRow = (topRow + bottomRow)//2
            # compare target to last row and first row
            if target > matrix[middleRow][-1]:
                topRow = middleRow + 1
            elif target < matrix[middleRow][0]:
                bottomRow = middleRow - 1
            else:
                break

        if not topRow <= bottomRow:
            return False

        middleRow = (topRow + bottomRow)//2
        print("final middleRow is correct =", middleRow)
        
        # 0, len(matrix[row]) -1
        leftCol, rightCol = 0, len(matrix[middleRow]) - 1

        # while loop to find middle column between left and right columns
        while leftCol <= rightCol:
            middleCol = (leftCol + rightCol)//2
            # compare target to last col to first col
            if target > matrix[middleRow][middleCol]:
                leftCol = middleCol + 1
            elif target < matrix[middleRow][middleCol]:
                rightCol = middleCol - 1
            else:
                return True
        return False

sol = Solution()
matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
target = 10
print("sol.twoDegreeMatrix()=", sol.twoDegreeMatrix(matrix, target))
# Output: true

print("***************** \n\n\n")
matrix=[[-8],[-3],[0],[4],[9]]
target=-3
print("sol.twoDegreeMatrix()=", sol.twoDegreeMatrix(matrix, target))
# Output: true

