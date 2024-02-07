def calculate_running_average(nums):
    result = []
    total = 0
    for i in range(len(nums)):
        total += nums[i]
        result.append(total / (i + 1))
    return result


lst = [1, 2, 3, 4, 5]

print(calculate_running_average(lst))