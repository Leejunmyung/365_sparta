import sys

t = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().strip()[:t])) for i in range(t)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cp_num = 0
house = []


def dfs(x, y):
    global cp_num
    matrix[x][y] = 0
    cp_num += 1
    for k in range(4):
        tx = x + dx[k]
        ty = y + dy[k]
        if tx < 0 or tx >= t or ty < 0 or ty >= t:
            continue
        if matrix[tx][ty] == 1:
            dfs(tx, ty)


for i in range(t):
    for j in range(t):
        if matrix[i][j] == 1:
            cp_num = 0
            dfs(i, j)
            house.append(cp_num)
house.sort()
print(len(house))
for i in house:
    print(i)
