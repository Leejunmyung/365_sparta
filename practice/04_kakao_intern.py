n = 4
start = 1
end = 4
roads = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
traps = [2, 3]

def solution(n,start,end,roads,traps):
    answer = 0
    current_num = 0
    for i in range(n-1):
        if start == roads[i][0]:
            current_num = roads[i][1]
            answer += roads[i][2]
        if current_num in traps:
            for j in range(n-1):
                roads[j][0],roads[j][1] = roads[j][1],roads[j][0]
                print(roads)
    return current_num

print(solution(n,start,end,roads,traps))