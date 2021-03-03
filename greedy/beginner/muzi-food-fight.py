# Muzi Food Fight Problem(Kakako)
# (30m, 1s, 128MB)
# O(k), 1 <= k <= 2e13

def solution(food_times, k):
    answer = 0
    current_index = 0

    last_index = -2
    for i in range(current_index, len(food_times)):
        if food_times[i] != 0:
            last_index = i
            break
    if last_index == -2:
        for i in range(0, current_index):
            if food_times[i] != 0:
                last_index = i
                break

    return last_index + 1


answer = solution([3, 1, 2], 5)
print(answer)
