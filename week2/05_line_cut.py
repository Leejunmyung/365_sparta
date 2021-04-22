import sys
k, n = map(int, sys.stdin.readline().split())
line = []
result = 0

for i in range(k):
    r = int(sys.stdin.readline())
    line.append(r)

current_max = max(line)
current_min = 0
current_try = (current_min + current_max) // 2

while current_min <= current_max:
    current_sum = sum([j // current_try for j in line])

    if current_sum >= n:
        result = current_try
        current_min = current_try + 1
    elif current_sum < n:
        current_max = current_try - 1
    current_try = (current_min + current_max) // 2
print(result)
