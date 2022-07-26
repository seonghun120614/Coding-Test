import math

def solution(n) :
    chk = False
    for i in range(int(math.log2(n)), -1, -1) :
        if n > 2**i :
            n -= 2**i
            chk = not chk

    print(int(chk))

solution(int(input()))