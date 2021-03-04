# Sort String Problem

data = [i for i in input()]

string = []
number = []

for item in data:
    if item.isdigit():
        number.append(int(item))
    else:
        string.append(item)

number_sum = sum(number)
string.sort()
solution = "".join(string) + str(number_sum)
print(solution)
