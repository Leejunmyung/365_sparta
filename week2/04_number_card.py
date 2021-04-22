import sys
t = int(sys.stdin.readline())
num_card = list(map(int, sys.stdin.readline().split()[:t]))
n = int(sys.stdin.readline())
compare_card = list(map(int, sys.stdin.readline().split()[:n]))
result = [0] * n
for i in range(len(compare_card)):
    for j in range(len(num_card)):
        if compare_card[i] == num_card[j]:
            result[i] += 1
        else:
            continue

for z in result:
    print(z, end=' ')

