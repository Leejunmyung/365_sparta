t = int(input("테스트 케이스: "))
result = []

for i in range(t):
    x = int(input("숫자 입력: "))
    result.append(x)
    result.sort()

for j in range(len(result)):
    print(result[j])
