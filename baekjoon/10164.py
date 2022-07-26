import math
from functools import reduce

def combination(n, r) :
    if r==0 or r==n : return 1
    return int(reduce(lambda x, y : x*y, range(n-r+1, n+1))/math.factorial(r))

r, c, k = list(map(int, input().split()))

if k%c==0 :
    pos1, pos2 = (k//c - 1)%r, c-1
    print(combination(pos1 + pos2, pos2))
else :
    pos1, pos2 = k//c, k%c - 1
    print(combination(pos1 + pos2, pos2)*combination(r+c-2-pos1-pos2, r-pos1-1))