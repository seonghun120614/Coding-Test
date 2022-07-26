from sys import stdin
from collections import deque

input = stdin.readline

def solution(n, idx) :
    
    imp = deque(enumerate(map(int, input().split())))
    target = imp[idx]
    i=n
    res = 0
    while res != target :
        prev = max(range(i), key = lambda x:imp[x][1])
        imp.rotate(-prev)
        res = imp.popleft()
        i-=1
    
    return n-i

res = ""
for _ in range(int(input())) :
    res += f"{solution(*tuple(map(int, input().split())))}\n"

print(res.rstrip())