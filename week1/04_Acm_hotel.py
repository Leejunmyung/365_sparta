t = int(input("테스트 케이스: "))

for z in range(t):
    h, w, n = map(int,input("층수,방수,몇번째 손님: ").split())
    hotel = []
    for i in range(1,w+1):
        for j in range(1,h+1):
            room_num = (j*100) + i
            hotel.append(room_num)
    print(hotel[n-1])


