import sys
t = int(input())

for _ in range(t):
    m,n,k = map(int,sys.stdin.readline().split())
    organic_list = [list(0 for j in range(n)) for i in range(m)]
    for n in range(k):
        x,y = map(int,sys.stdin.readline().split())
        organic_list[x][y] += 1


    for i in range(len())