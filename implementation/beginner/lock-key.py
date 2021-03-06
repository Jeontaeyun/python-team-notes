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

def check_can_lock(lock, key, row, column):
    n = len(lock)
    key_row_length = len(key)
    key_column_length = len(key[0])
    for r in range(n):
        for c in range(n):
            if r >= row and c >= column and (r-row) < key_row_length and (c-column) < key_column_length:
                if lock[r][c] ^ key[r-row][c-column] == 0:
                    return False
            else : 
                if lock[r][c] == 0:
                    return False
    return True
  


def solution(key, lock):
    answer = False
    n = len(lock)
    m = len(key)
    for lock_row in range(n):
        for lock_column in range(n):
            # ! 연산의 순서가 중요하다. 배열을 회전하는 것이 비용이 가장 많이들기 때문에 최대한 나중에 한다.
            for rotate in range(4):
                key = rotate_matrix_90deg(key)
                for key_row in range(m):
                    for key_column in range(m):
                        sliced_key = slice_2d_matrix(key, key_row, key_column)
                        result = check_can_lock(lock, sliced_key, lock_row, lock_column)
                        if result == True:
                            # ! 이 부분에서 바로 반환하면 연산 작업과 코드가 모두 줄어든다.
                            return True
    return False

result = solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])
print(result)
