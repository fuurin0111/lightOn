print("範囲を決めてください")
width,height = map(int, input().split())
map0,map_pre = [],[]
x,y = 0,0
end_num = 0
number_list = []
flag = True

for i in range(height):
    map_pre = []
    for j in range(width):
        map_pre.append(0)
    map0.append(map_pre)

for i in range(width):
    number_list.append(i+1)

def printer():
    print(*number_list)
    print()
    for i in range(height):
        print(*map0[i],"",i+1)

def change(num):
    if num == 0:
        return 1
    elif num == 1:
        return 0

printer()

try:
    while flag:
        print("どこのライトをオンにしますか？")
        x,y = map(int, input().split())
        map0[y-1][x-1] = change(map0[y-1][x-1])
        if x == 1 and y == 1:
            map0[y][x-1] = change(map0[y][x-1])
            map0[y-1][x] = change(map0[y-1][x])
        elif x == width and y == height:
            map0[height-2][width-1] = change(map0[height-2][width-1])
            map0[height-1][width-2] = change(map0[height-1][width-2])
        elif x == width and y == 1:
            map0[y-1][width-2] = change(map0[y-1][width-2])
            map0[y][width-1] = change(map0[y][width-1])
        elif x == 1 and y == height:
            map0[height-1][x] = change(map0[height-1][x])
            map0[height-2][x-1] = change(map0[height-2][x-1])
        elif x <= 1:
            map0[y-2][x-1] = change(map0[y-2][x-1])
            map0[y][x-1] = change(map0[y][x-1])
            map0[y-1][x] = change(map0[y-1][x])
        elif x >= width:
            map0[y-2][x-1] = change(map0[y-1][x-1])
            map0[y][x-1] = change(map0[y][x-1])
            map0[y-1][x-2] = change(map0[y-1][x-2])
        elif y <= 1:
            map0[y-1][x] = change(map0[y-1][x])
            map0[y-1][x-2] = change(map0[y-1][x-2])
            map0[y][x-1] = change(map0[y][x-1])
        elif y >= height:
            map0[y-1][x] = change(map0[y-1][x])
            map0[y-1][x-2] = change(map0[y-1][x-2])
            map0[y-2][x-1] = change(map0[y-2][x-1])
        else:
            map0[y-1][x] = change(map0[y-1][x])
            map0[y-1][x-2] = change(map0[y-1][x-2])
            map0[y-2][x-1] = change(map0[y-2][x-1])
            map0[y][x-1] = change(map0[y][x-1])

        printer()
        end_num = 0
        for i in range(height):
            if not(0 in map0[i]):
                end_num += 1
        
        if end_num >= height:
            print("クリア!")
            flag = False

except KeyboardInterrupt:
    print("終了します")