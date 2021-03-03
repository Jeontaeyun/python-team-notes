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
            # 이렇게 각 배열을 매번 제거해주면 중간중간에 배열 연산이 들어가 O(XK) 효율성 문제에서 통과할 수 없다.
            # 효율성 문제가 들어간 알고리즘은 최대한 연산의 횟수를 높이는 것 보다 상수로 계산할 수 없는지 고민하는 것이 좋다.
            for i in range(0, len(q)):
                q[i][0] -= rest_time
            if k == 0:
                break
        else:
            heapq.heappush(q, [rest_time, index])
            break

    q = sorted(q, key=lambda x: x[1])
    last_index = k % len(q)
    answer = q[last_index]
    return answer[1]


answer = solution([3, 1, 1], 4)
print(answer)
