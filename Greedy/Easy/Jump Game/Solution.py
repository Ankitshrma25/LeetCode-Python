class Solution:
    def canJump(self, nums):
        return self.is_reachable(nums)


    def is_reachable(self, nums):
        max_reach = 0
        
        for index in range(len(nums)):
            if self.is_stuck(index, max_reach):
                return False
            
            max_reach = self.update_reach(index, nums[index], max_reach)
        
        return True


    def is_stuck(self, index, max_reach):
        return index > max_reach


    def update_reach(self, index, jump, max_reach):
        return max(max_reach, index + jump)
