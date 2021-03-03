# Muzi Food Fight Problem(Kakako)
# (30m, 1s, 128MB)
# O(k), 1 <= k <= 2e13
# 문제를 풀 때 손부터 갖다 대지말고 최대한 글로 정리한 후 순차적으로 개발을 진행하자.

import heapq


def solution(food_times, k):
    q = []
    answer = 0
    current_index = 0

    if sum(food_times) <= k:
        return -1

    for i in range(0, len(food_times)):
        heapq.heappush(q, [food_times[i], i+1])

    sum_value = 0  # 먹기 위해 사용한 시간
    previous = 0  # 직전에 다 먹은 음식 시간
    length = len(food_times)  # 남은 음식의 개수

    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now-previous) * length
        length -= 1  # 다 먹은 음식 제외
        previous = now

    result = sorted(q, key=lambda x: x[1])
    return result[(k - sum_value) % length][1]


answer = solution([3, 1, 1], 4)
print(answer)
