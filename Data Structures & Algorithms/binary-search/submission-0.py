class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # In: int[] nums, sorted and distinct. int target
        # Out: int, index of target OR -1 if target isn't found
        # Con:
        # - Solution must run in O(logn) time --> Must use BST
        # Edge:
        # - Empty array? --> Not possible
        # - Invalid input? --> Not possible

        left = 0
        right = len(nums)-1
        mid = (left+right)//2

        while left <= right:
            curr_num = nums[mid]
            if curr_num < target:
                left = mid+1
            elif curr_num > target:
                right = mid-1
            else:
                return mid
            mid = (left+right)//2
        
        return -1