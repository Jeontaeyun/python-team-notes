# Minimum Unavailable Coin Problem
# (30m, 128MB)
# 부분 집합을 만드는 로직에 대해서 파악하는 것이 중요하다.
# 1 <= N <= 1,000

n = int(input())
data = list(map(int, input().split()))
flag = [0] * n

power_set_sum_list = []
# Powerset은 2^n -1 의 개수를 가진다.


def make_power_set(flag, index):
    if n == index:
        sum = 0
        for i in range(0, n):
            if flag[i] == True:
                sum += data[i]
        power_set_sum_list.append(sum)
        return
    flag[index] = 1
    make_power_set(flag, index+1)
    flag[index] = 0
    make_power_set(flag, index+1)


make_power_set(flag, 0)
power_set_sum_list = sorted(power_set_sum_list)

result = 0

for i in range(1, power_set_sum_list[-1]):
    if result != 0:
        break
    same = False
    for value in power_set_sum_list:
        if value == i:
            same = True
            break
    if same == False:
        result = i

print(result)
