def longestOne(nums, k):
    left = 0
    max_length = 0
    count_zero = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            count_zero += 1
        while count_zero > k:
            if nums[left] == 0:
                count_zero -= 1
            left += 1
            
        max_length = max(max_length, right - left + 1)
    return max_length

