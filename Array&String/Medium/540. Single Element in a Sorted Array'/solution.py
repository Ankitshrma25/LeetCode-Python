class solution:
    def singalNonDuplicate(nums):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            
            if nums[mid - 1] == nums[mid]:
                low = mid + 1
            elif nums[mid + 1] == nums[mid]:
                high = mid - 1
            else:
                return nums[mid]
            