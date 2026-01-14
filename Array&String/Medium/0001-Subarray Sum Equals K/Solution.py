from typing import List

class Solution:
    
    def initialize_map(self):
        # Stores prefix sum frequencies
        return {0: 1}
    
    def update_count(self, mp, current_sum, k):
        # Check if required sum exists
        return mp.get(current_sum - k, 0)
    
    def update_map(self, mp, current_sum):
        # Update frequency of current prefix sum
        mp[current_sum] = mp.get(current_sum, 0) + 1
    
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixsum = 0
        count = 0
        mp = self.initialize_map()

        for num in nums:
            prefixsum += num
            
            count += self.update_count(mp, prefixsum, k)
            self.update_map(mp, prefixsum)

        return count
