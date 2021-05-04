putin = [[100, 95, 100, 70, 65], [85, 60, 70, 94, 65],[90,80,60,75,60]]


def solution(array):
    answer = ""
    for i in range(len(array)):
        result = 0
        pra = len(array[i])
        if array[i][i] == min(array[i]) or array[i][i] == max(array[i]):
            if array[i].count(array[i][i]) == 1 or array[i].count(array[i][i]) == 1:
                array[i].pop(i)
                result = (sum(array[i])//pra)
            else:
                result = (sum(array[i])//pra)
        else:
            result = (sum(array[i]))//pra

        if result >= 90:
            answer += "A"
        elif result >= 80:
            answer += "B"
        elif result >= 70:
            answer += "C"
        elif result >= 50:
            answer += "D"
        else:
            answer += "F"
    return answer

print(solution(putin))
