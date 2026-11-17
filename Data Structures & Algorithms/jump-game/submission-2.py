class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        def bestJump(position, maxJump):
            best = 0
            best_jump = position
            for i in range(1,maxJump+1):
                if best < i + nums[position+i]:
                    best = i + nums[position+i]
                    best_jump = position + i
            return best_jump

        position = 0
        while nums[position] != 0:
            if position + nums[position] >= len(nums)-1:
                return True
            position = bestJump(position, nums[position])

        return False

[1,2,0,1,0]
