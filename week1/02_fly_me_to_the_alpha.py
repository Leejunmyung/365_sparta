t = int(input("테스트 케이스:"))
result = []

for i in range(t):
    x, y = map(int, input("숫자 입력: ").split(","))
    z = y - x
    v = int(z**(1/2)) + 1
    down = (v - 1) * (v - 1)
    up = v * v
    stand = (up + down) / 2

    if stand > z:
        result.append(v * 2 -2)
    else:
        result.append(v * 2 -1)

print(result)
