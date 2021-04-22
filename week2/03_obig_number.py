import sys
t = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

for i in range(0, t):
    cur = num.pop(0)
    for j in range(len(num)):
        if cur < num[j]:
            print(num[j])
            break
    else:
        print(-1)







