from typing import List, Tuple

# 1. Activity Selection (Max non-overlapping intervals)
def max_activities(intervals: List[Tuple[int, int]]) -> int:
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[1])  # sort by end time

    count = 1
    last_end = intervals[0][1]

    for start, end in intervals[1:]:
        if start >= last_end:
            count += 1
            last_end = end

    return count


# 2. Fractional Knapsack
def fractional_knapsack(values: List[int], weights: List[int], capacity: int) -> float:
    items = [(v / w, v, w) for v, w in zip(values, weights)]
    items.sort(reverse=True)  # sort by value/weight

    total_value = 0

    for ratio, value, weight in items:
        if capacity >= weight:
            total_value += value
            capacity -= weight
        else:
            total_value += ratio * capacity
            break

    return total_value


# 3. Assign Cookies (Greedy)
def assign_cookies(greed: List[int], cookies: List[int]) -> int:
    greed.sort()
    cookies.sort()

    i = j = 0
    satisfied = 0

    while i < len(greed) and j < len(cookies):
        if cookies[j] >= greed[i]:
            satisfied += 1
            i += 1
        j += 1

    return satisfied


# 4. Jump Game
def can_jump(nums: List[int]) -> bool:
    max_reach = 0

    for i in range(len(nums)):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + nums[i])

    return True  
