class Solution:
    def findMin(self, nums: List[int]) -> int:
        # In: int[] nums, rotated anywhere between 1 and len(nums) times
        # Out: smallest number in nums

        # Con:
        # Rotated --> every element was shifted to the left. (leftmost element get re-appended)
        # Every element is unique
        # nums was originally sorted.
        # Need O(log n) time complexity solution.
        # nums is between 1 and 1000 numbers long. --> No empty array edge case

        # Edge:
        # Array length of 1? --> Return nums[0]

        # Brute Force method: Start at beginning, iterate through all elements, use variable to track minimum.
        # --> O(n) time.

        # Binary Search method
        # Original array is sorted --> we can iterate half of the remaining list at a time
        # How should each iteration look?
        # Compare the middle to the left and right boundaries.
        # middle < left --> The minimum is between the left and mid! (OR middle is min) --> Move the right boundary backward
        # middle > right --> The minimum is between the mid and right! --> Move the left bounary forward
        # left < middle < right --> The minimum is the left! return element at the left boundary.
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left+right) // 2
            print(left, right, mid)
            if nums[mid] < nums[left]:
                if nums[mid] < nums[mid-1]:
                    return nums[mid]
                right = mid - 1
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                return nums[left]
        
        return nums[left]