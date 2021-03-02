# Multiple or Add Problem
# Greedy Solution : Add only when string is zero

data = str(input())

result = 0

for number in data:
    add_case = result + int(number)
    multiple_case = result * int(number)
    if add_case > multiple_case:
        result = add_case
    else:
        result = multiple_case

print(result)
