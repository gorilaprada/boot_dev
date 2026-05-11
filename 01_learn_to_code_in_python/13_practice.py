"""
# Lesson 1
def number_sum(n):
    final_sum = 0
    for i in range(0, n+1):
        final_sum += i
    return final_sum
#
# Lesson 2
def find_min(nums):
    min_so_far = float("inf")
    for num in nums:
        if num < min_so_far:
            min_so_far = num
        else:
            continue
    return min_so_far
#
# Lesson 3
def remove_nonints(nums):
    new_nums = []
    for num in nums:
        if int != type(num):
            continue
        elif int == type(num):
            new_nums.append(num)
    return new_nums
# Lesson 4
def factorial(num):
    if num < 0:
        return "cannot do factorial on negative numbers"
    if num == 0:
        return 1
    result = num
    for i in range(num - 1, 0, -1):
        result = result * i
    return result
# Lesson 5
def area_sum(rectangles):
    sum_of_areas = 0
    for rectangle in rectangles:
        current_area = rectangle["height"] * rectangle["width"]
        sum_of_areas += current_area
    return sum_of_areas
# Lesson 6
def divide_list(nums, divisor):
    new_list = []
    for num in nums:
        new_list.append(num / divisor)
   return new_list
# Lesson 7
def join_strings(strings):
    joined_string = ""
    if not strings:
        return ""
    for i in range(0, len(strings)):
        joined_string += strings[i] + ","
    joined_string = joined_string[:-1]
    return joined_string
# Lesson 8
run_cases = [
    {
        "luck_boosts": [],
        "expected_avg": 0.0,
    },
    {
        "luck_boosts": [5, 3, 10],
        "expected_avg": 6.0,
    },
    {
        "luck_boosts": [7],
        "expected_avg": 7.0,
    },
    {
        "luck_boosts": [4, 4, 4],
        "expected_avg": 4.0,
    },
    {
        "luck_boosts": [2, 3],
        "expected_avg": 2.5,
    },
]
"""
# Lesson 9
def avg_luck_boost(luck_boosts):
    if not luck_boosts:
        return 0.0
    total = 0
    for boost in luck_boosts:
        total += boost
    return total / len(luck_boosts)
