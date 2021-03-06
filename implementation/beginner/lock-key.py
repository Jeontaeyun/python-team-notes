# Lock and Key problem
# https://programmers.co.kr/learn/courses/30/lessons/60059
# 40m, 1s, 128MB
# [제약 사항] 자물쇠 영역을 벗어난 부분에 있는 열쇠의 홈과 돌기는 자물쇠를 여는 데 영향을 주지 않지만,
# 자물쇠 영역 내에서는 열쇠의 돌기 부분과 자물쇠의 홈 부분이 정확히 일치해야 하며 열쇠의 돌기와 자물쇠의 돌기가 만나서는 안됩니다.
# Brute-Force 완전 탐색 문제라고 예상 M*M, N*N 배열에서  3 <= M, N <= 20 -> 모든 경우의수를 해도 400 * 400 * 4 = 640,000회 반복(무난)
# 1(key) ^ 1(lock) = 0
# 1(key) ^ 0(lock) = 1
# 0(key) ^ 1(lock) = 1
# 0(key) ^ 0(lock) = 0
# XOR을 해서 파악

# ! Rotate Matrix 90deg function
def rotate_matrix_90deg(matrix):
    n = len(matrix)
    result = [[0] * n for _ in range(n) ]

    for row in range(n):
        for column in range(n):
            result[column][n-1-row] = matrix[row][column]
    return result

# ! Slice 2d Matrix with row, column
def slice_2d_matrix(matrix, row, column):
    n = len(matrix)-row
    m = len(matrix[0])-column
    result = [[0] * m for _ in range(n)]
    for i in range(0, n):
        for j in range(0, m):
            result[i][j] = matrix[row + i][column + j] 
    return result



def solution(key, lock):
    answer = False
    n = len(lock);
    m = len(key);
    result = [[0] * n for _ in range(n)]
    for lock_row in range(n):
        for lock_column in range(n):
            for key_row in range(m):
                for key_column in range(m):

    return answer

print([[0, 0, 0], [1, 0, 0], [0, 1, 1]] + [[1, 1, 1], [1, 1, 0], [1, 0, 1]])
#result = solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])
#print(rotate)
