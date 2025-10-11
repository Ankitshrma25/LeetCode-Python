from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ## Hash table approach
        # Create an empty set
        set = set()
        # check if any item of list is present in the set or not
        for num in nums:
            # Checking if num is present in the set or not
            if num in set:
                return True
            set.add(num)
        # If there is no num is present already in the set then no duplicate 
        return False