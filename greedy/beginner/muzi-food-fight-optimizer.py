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

    while True:
        rest_time, index = heapq.heappop(q)
        subtract_time = (len(q)+1) * rest_time
        if subtract_time <= k:
            k -= subtract_time
            subtract_list = []
            for i in range(0, len(q)):
                q[i][0] -= rest_time
            if k == 0:
                break
        else:
            heapq.heappush(q, [rest_time, index])
            break

    q = sorted(q, key=lambda x: x[1])
    print(k, q)
    last_index = k % len(q)
    answer = q[last_index]
    return answer[1]


answer = solution([3, 1, 1], 4)
print(answer)
