# Luck Straight
# 20m, 1s, 256MB
# Simulation

n = [int(i) for i in input()]

length = len(n)
half_index = length // 2

left_sum = sum(n[0:half_index])
right_sum = sum(n[half_index: length])

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")
