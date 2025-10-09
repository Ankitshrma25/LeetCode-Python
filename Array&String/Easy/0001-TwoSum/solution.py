from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        # checking for the index first of the array and then the second one 
        for i in range(n):
            for j in range(i+1, n):
                # checking the sum of both indexes to be equal to the target or not
                if nums[i] +nums[j] == target:
                    return [i, j]
        # Returning an empty list if no such pair is found.        
        return []
            