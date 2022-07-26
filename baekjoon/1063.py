from sys import stdin

input = stdin.readline

order = {
    "R":(1, 0),
    "L":(-1, -0),
    "B":(0, -1),
    "T":(0, 1),
    "RT":(1, 1),
    "LT":(-1, 1),
    "RB":(1,-1),
    "LB":(-1,-1)
}

def pos_trans(s) :
    x = ord(s[0])-64
    y = int(s[1])
    return x, y

def chr_trans(x, y) :
    return f"{chr(x+64)}{y}"

def chk(x, y) :
    return 0<x<9 and 0<y<9

king, stone, n = input().split()

kx, ky = pos_trans(king)
sx, sy = pos_trans(stone)

for _ in range(int(n)) :
    dx, dy = order[input().rstrip()]
    tmp1, tmp2 = kx + dx, ky + dy
    
    if chk(tmp1, tmp2) :
        if tmp1 == sx and tmp2 == sy :
            if chk(sx+dx, sy+dy) :
                kx, ky = sx, sy
                sx+=dx
                sy+=dy
            else :
                continue
        else :
            kx, ky = tmp1, tmp2
    else :
        continue

print(chr_trans(kx, ky)+"\n"+chr_trans(sx, sy))