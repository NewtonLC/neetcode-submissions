class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # In: m x n 2D int[][] matrix, int target
        # Out: T/F
        # Objective: Search the matrix for the target, return True if exists, False otherwise
        # Con:
        # - O(log(n * m)) runtime --> BST
        # Edge:
        # - Empty array --> False
        # - Invalid inputs? --> Don't consider

        # Plan: BST
        # Define middle with respect to 2D array.
        #  - Let's say I want to access "index 5"
        #  - outer index --> index // row length, inner index --> index % row length.
        # Look at middle, compare to target
        
        if not matrix:
            return False
        if not matrix[0]:
            return False

        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = (m * n) - 1

        while left <= right:
            middle = (left+right) // 2
            o_ind = middle // n
            i_ind = middle % n
            if matrix[o_ind][i_ind] > target:
                right = middle - 1
            elif matrix[o_ind][i_ind] < target:
                left = middle + 1
            else:
                return True
        
        return False