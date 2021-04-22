import sys
t = int(sys.stdin.readline())
result = []

for i in range(t):
    num = int(sys.stdin.readline())
    if num == 0:
        out_num = result.pop()
    else:
        result.append(num)
print(sum(result))
