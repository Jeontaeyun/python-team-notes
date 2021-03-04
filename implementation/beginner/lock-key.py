# Lock and Key problem
# https://programmers.co.kr/learn/courses/30/lessons/60059
# 40m, 1s, 128MB
# [제약 사항] 자물쇠 영역을 벗어난 부분에 있는 열쇠의 홈과 돌기는 자물쇠를 여는 데 영향을 주지 않지만,
# 자물쇠 영역 내에서는 열쇠의 돌기 부분과 자물쇠의 홈 부분이 정확히 일치해야 하며 열쇠의 돌기와 자물쇠의 돌기가 만나서는 안됩니다.

def solution(key, lock):
    answer = True
    return answer


result = solution([[0, 0, 0], [1, 0, 0]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])
print(result)
