import math
from sys import stdin

def is_primary(start, end) :
    res = 0
    lst = []
    for i in range(start, end+1) :
        if i==1 : continue
        
        tmp, chk = 2, True
        
        while tmp <= math.sqrt(i):
            if i%tmp==0 :
                chk = False
                break
            tmp+=1
        
        if chk :
            lst.append(i)
            res += i
    
    if res == 0 : 
        print(-1)
    else :
        print(res, lst[0], sep="\n")

input = stdin.readline
is_primary(int(input()), int(input()))