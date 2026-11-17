class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_hash = {}

        for i in range(len(nums)):
            difference = target-nums[i]
            if difference in nums_hash:
                return [nums_hash[difference], i]
            nums_hash[nums[i]] = i

        return
        