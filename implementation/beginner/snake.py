# Snake Problem
# 40m 1s 128MB Samsung SW test
#

n = int(input())
k = int(input())
# RIGHT -> BOTTOM -> LEFT -> TOP | right-rotate = +1 , left-rotate = -1
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

snake_map = [[0] * n for _ in range(n)]
for _ in range(k):
    row, column = input().split()
    snake_map[int(row) - 1][int(column) - 1] = 2

L = int(input())
commands = []

for _ in range(L):
    second, command = input().split()
    commands.append((second, command))

time = 0
current_direction = 0
result = 0
current_row = 0
current_column = 0
snake_position = [(0, 0)]
snake_map[0][0] = 1
while True:
    time += 1
    next_r, next_c = direction[current_direction]
    next_row = next_r + current_row
    next_column = next_c + current_column
    print(snake_position)
    if next_row >= n or next_column >= n or next_row < 0 or next_column < 0:
        print(time)
        break
    if snake_map[next_row][next_column] == 1:
        print(time)
        break
    if snake_map[next_row][next_column] == 2:
        snake_map[next_row][next_column] == 1
        current_row = next_row
        current_column = next_column
        snake_position.append((next_row, next_column))
    else:
        snake_map[next_row][next_column] == 1
        current_row = next_row
        current_column = next_column
        snake_position.append((next_row, next_column))

        tail_row, tail_column = snake_position.pop(0)
        snake_map[tail_row][tail_column] = 0
        
    command_length = len(commands)
    for i in range(0, command_length):
        if int(commands[i][0]) == time:
            if commands[i][1] == 'L':
                current_direction -= 1
                if current_direction <= 0:
                    current_direction = 3
            elif commands[i][1] == 'D':
                current_direction += 1
                if current_direction >= 4:
                    current_direction = 0
            commands.pop(0)
            break
