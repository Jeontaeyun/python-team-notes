# Adventurer Guild
# Time Limit 30m, Memory Limit 128MB

n = int(input())
fear_list = list(map(int, input().split()))

feat_list = fear_list.sort()
dictionary = {}

result = 0

for i in range(0, n):
    if dictionary.get(fear_list[i]) == None:
        dictionary[fear_list[i]] = 1
    else:
        dictionary[fear_list[i]] += 1

for key in dictionary:
    result += dictionary[key] // key


print(result)
