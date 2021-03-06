## 👋🏻 Implementation

> 구현 유형(Implementation)은 생각하기는 상대적으로 쉬우나, 이를 코드로 구현함에 있어서 여러가지 장애물이 존재하는 알고리즘이다. 자신이 사용하는 언어에 충실히 익숙하고 자신의 생각을 코드로 작성할 수 있다면 쉬운 문제이다.

### Main Problem

- Brute-Force Search(using loop or recursive function)
- Simulation

### Simulation

> 시뮬레이션(Simulation)은 어떤 문제를 해결하기 위하여 실제현상의 본질을 나타내는 모형을 만들어 실험하고, 얻은 결과를 이용하여 실제현상의 특성을 설명하고 예측하는 의사결정 기법을 말함


## ⚙️ Utility

해당 파트의 문제를 풀면서 2차원 배열을 다루는 것에 대한 다양한 생각을 할 수 있었다. 
특히 배열을 회전하는 함수나, 특정 부분을 슬라이스 하는 함수는 유용할 것이라 생각해서 별도의 코드로 분리했다.

### rotate_matrix_90deg
행렬을 90도씩 회전하는 함수입니다. 시계 방향 90도입니다.

```python
def rotate_matrix_90deg(matrix):
    n = len(matrix)
    result = [[0] * n for _ in range(n) ]

    for row in range(n):
        for column in range(n):
            result[column][n-1-row] = matrix[row][column]
    return result
```

### slice_matrix
특정 열과 행을 기준으로 행렬을 자르는 함수입니다.
```python
def slice_matrix(matrix, row, column):
    n = len(matrix)-row
    m = len(matrix[0])-column
    result = [[0] * m for _ in range(n)]
    for i in range(0, n):
        for j in range(0, m):
            result[i][j] = matrix[row + i][column + j] 
    return result
```

### list_chunk
1차원 리스트를 n개의 항목으로 덩어리화(Chunk)하는 함수입니다.
```python
def list_chunk(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]
```
