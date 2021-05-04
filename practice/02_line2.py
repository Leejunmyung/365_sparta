putin = [3,5,4,1,2]

def solution(array):
    compare = []
    index = []
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] < array[j]:
                compare.append(j)
                index.append(min(compare))
                compare.clear()
    return  index

print(solution(putin))