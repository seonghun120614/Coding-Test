import math
from sys import stdin

def primary_cnt(lst, n) :
    cnt = n
    for i in lst :
        if i<2 :
            cnt-=1
            continue
        else :
            tmp = 2
            rng = math.sqrt(i)
            while tmp<=rng :
                if i%tmp==0 :
                    cnt-=1
                    break
                tmp+=1
    return cnt

input = stdin.readline
n, lst = int(input()), list(map(int, input().split()))
print(primary_cnt(lst, n))