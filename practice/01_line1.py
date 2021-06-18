putin = "line [({<plus>)}]"


def solution(string):
    stack = []
    compare = ["()", "{}", "[]", "<>"]
    correct = 0
    for i in range(len(string)):
        if string[i] == "[" or string[i] == "(" or string[i] == "{" or string[i] == "<":
            stack.append(string[i])
        elif string[i] == "]" or string[i] == "}" or string[i] == ")" or string[i] == ">":
            gal = stack.pop() + string[i]
            if i == 0:
                return -i
            elif len(stack) == 0 or gal not in compare:
                return -i
            elif gal in compare:
                correct += 1
        else:
            return -i

    if len(stack) != 0:
        return -(len(string)-1)


print(solution(putin))
