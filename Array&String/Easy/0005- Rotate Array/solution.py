'''
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
'''

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        l, r = 0, len(nums) - 1
        # Reverse the whole array
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
        # Reverse first part of the array sepersted by k
        l, r = 0, k-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
        # Reverse the second half of the array above k
        l, r = k, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1


if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3,5,6,4,5,6,7,3]
    k=4
    sol.rotate(nums,k)

    print(nums)
