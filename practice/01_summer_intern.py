company_code = "012345"
day = "20190620"
data = ["price=80 code=987654 time=2019062113","price=90 code=012345 time=2019062014",
        "price=120 code=987654 time=2019062010","price=110 code=012345 time=2019062009",
        "price=95 code=012345 time=2019062111"]

def solution(code, day, data):
    extraction = []
    for i in range(len(data)):
        if code in data[i] and day in data[i]:
            extraction.append(data[i][6:].split())
    for j in range(2):
        extraction[j].pop()
        extraction[j].pop()
    answer = extraction[0] + extraction[1]
    answer.sort()
    answer = list(map(int,answer))
    return answer

print(solution(company_code,day,data))