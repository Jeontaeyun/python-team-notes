def solution(food_times, k):
    answer = 0
    current_index = 0
    for i in range(0, k):
        while True:
            if sum(food_times) == 0:
                break
            if food_times[current_index] != 0:
                food_times[current_index] -= 1
                current_index += 1
                if current_index == (len(food_times)):
                    current_index = 0
                break
            else:
                current_index += 1
                if current_index == (len(food_times)):
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
