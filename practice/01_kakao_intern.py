s= "one4seveneight"

def solution(s):
    answer = 0
    result = []
    eng_num = {
        "zero": 0, "one": 1, "two": 2,"three":3,"four":4,"five":5,"six":6,
        "seven":7, "eight":8, "nine":9}

    for i in eng_num:
        if i in s:
            result.append(eng_num[i])
        elif str(eng_num[i]) in s:
            result.append(eng_num[i])
    for j in result:
        answer *= 10
        answer += j
    return answer
    # change = list(map(str,result))
    # answer = print(''.join(change))
    # return answer


print(solution(s))