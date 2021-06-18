places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
          ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"],
          ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

def solution(places):
    answer=[]
    p_location = [list() for i in range(5)]
    for x in range(5):
        for y in range(5):
            for z in range(5):
                if places[x][y][z] == 'P':
                    p_location[x].append([y,z])

    return p_location
print(solution(places))