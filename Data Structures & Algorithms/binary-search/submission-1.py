class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        in: int[] nums: integers are distinct, and sorted in ascending order.
            int target --> search for this in the nums array
        out: int, --> index of target OR -1 if it doesn't exist.

        con:
        - O(log n) time
        - all integers in nums are unique
        
        edge:
        - len 1 --> return nums[0] == target

        Plan: Brute Force Method
        Iterating through nums linearly --> O(n)

        Plan: Binary Search
        Iteration --> Remove half of the elements in nums --> O(log n)
        left, middle, right, (target)
        is middle > target? --> right boundary inwards
        is middle < target? --> left boundary inwards
        is middle == target? --> return middle

        (exit loop) --> return -1

        '''

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1