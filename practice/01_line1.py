putin = "line [({<plus>})"


def solution(string):
    stack = []
    compare = ["()", "{}", "[]", "<>"]
    correct = 0
    for i in range(len(string)):
        if string[i] == "[" or string[i] == "(" or string[i] == "{" or string[i] == "<":
            stack.append(string[i])
        elif string[i] == "]" or string[i] == "}" or string[i] == ")" or string[i] == ">":
            if len(stack) == 0:
                return correct
            gal = str(stack.pop() + string[i])
            if gal not in compare:
                return -i
            else:
                correct += 1
    if len(stack) != 0:
        return -(len(string)-1)

    return correct


print(solution(putin))
