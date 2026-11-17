class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # In: int[] nums, nums[i] represent maximum jump lengths
        # Out: True/False --> Can we reach the len(nums)-1 from 0?
        # Con:
        # - nums[i] is always nonnegative.
        # - nums must have at least 1 position --> []
        # - Always going in the same direction(left to right)
        # - When do we return false? --> nums[i] == 0 --> pit
        # Edge:
        # - nums has exactly 1 position? --> True
        
        # Plan: Brute Force
        # Start at index 0
        # Test out every possible path from 0.

        # Plan: Greedy Approach
        # We can only move in one direction, and we want to maximize potential.
        # We can split this problem into many sub-problems. --> What is the most efficient jump from my one location?
        # Constant space, O(n^2) 

        # Why O(n^2)
        # [4,4,4,4,4,0,0,0,0,0] --> False
        # 1 + 4 --> 5
        # 2 + 4 --> 6
        # 3 + 4 --> 7
        # 4 + 4 --> 8

        # Plan: Greedy Approach, iterate backwards.
        # [1]
        # O(n) time

        # Algorithm:
        goal = len(nums)-1

        for i in range(len(nums)-2, -1, -1):
            if nums[i] + i >= goal:
                goal = i

        return goal == 0