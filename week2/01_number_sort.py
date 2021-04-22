import sys
t = int(sys.stdin.readline())
result = []

for i in range(t):
    x = int(sys.stdin.readline())
    result.append(x)
    result.sort()

for j in range(len(result)):
    print(result[j])
