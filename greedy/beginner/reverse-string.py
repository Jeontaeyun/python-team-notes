# Revers String Problem
# TIme Limit 20m, Memory Limit 128MB

string = str(input())

zero_line = 0
one_line = 0
previous_number = -1

for i in string:
    if previous_number == -1:
        previous_number = int(i)
        if int(i) == 1:
            one_line += 1
        else:
            zero_line += 1

    if previous_number != int(i):
        previous_number = int(i)
        if int(i) == 1:
            one_line += 1
        else:
            zero_line += 1

result = min(zero_line, one_line)
print(result)
