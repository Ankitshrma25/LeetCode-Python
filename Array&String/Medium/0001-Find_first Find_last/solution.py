from typing import List

def find_first(nums: List[int], target: int) -> int:
    low, high = 0, len(nums) - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            ans = mid
            high = mid - 1   # search left
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return ans


def find_last(nums: List[int], target: int) -> int:
    low, high = 0, len(nums) - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            ans = mid
            low = mid + 1    # search right
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return ans


def search_range(nums: List[int], target: int) -> List[int]:
    first = find_first(nums, target)
    last = find_last(nums, target)
    return [first, last]


# Testing block
if __name__ == "__main__":
    test_cases = [
        ([5,7,7,8,8,10], 8),
        ([5,7,7,8,8,10], 6),
        ([], 0),
        ([1], 1)
    ]

    for nums, target in test_cases:
        print(nums, target, "->", search_range(nums, target))
