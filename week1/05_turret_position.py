t = int(input())
result = 0
for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    m_x = x1 - x2
    m_y = y1 - y2
    d = (m_x**2 + m_y**2)**0.5
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            result = -1
        else:
            result = 0
    if r1+r2 < d or r1-r2 > d:
        result = 0
    elif r1+r2 == d or r1-r2 == d:
        result = 1
    elif r1-r2 < d < r1+r2 and x1 != x2 or y1 != y2:
        result = 2
    print(result)
