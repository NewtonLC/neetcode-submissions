class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        in: int[][], m x n, each row is non-decreasing, each row is greater than the last
        out: boolean, check if target exists, false if not.

        con:
        - O(log(m*n)) time
        - non-decreasing != ascending --> not every number is distinct
        - m, n >= 1

        edge:
        - 1 x 1 --> matrix[0][0] == target

        Plan:
        1. Brute Force Method
        Iterate through whole matrix --> O(m*n)

        2. Binary Search
        Scrap half the matrix per iteration --> O(log(m*n))

        Each iteration: mid, left, right, target
        is mid < target? --> move left boundary in
        if mid > target? --> move right boundary in
        is mid == target? --> return true

        [0][0], [1][1], [2][3]
        '''

        left = 0
        right = len(matrix) * len(matrix[0]) - 1

        while left <= right:
            mid = (left+right)//2

            x = mid // len(matrix[0])
            y = mid % len(matrix[0])

            if matrix[x][y] < target:
                left = mid + 1
            elif matrix[x][y] > target:
                right = mid - 1
            else:
                return True
        
        return False