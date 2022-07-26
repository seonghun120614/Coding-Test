from sys import stdin
from collections import deque
input = stdin.readline

def solution(n) :
    deq = deque(range(1, n+1))
    cnt = 0
    for i in list(map(int, input().split())) :
        while True :
            if deq[0] == i :
                deq.popleft()
                break
            else:
                if deq.index(i) < len(deq)/2 :
                    while deq[0] != i :
                        deq.rotate(-1)
                        cnt += 1
                else :
                    while deq[0] != i :
                        deq.rotate(1)
                        cnt += 1
    print(cnt)

solution(int(input().split()[0]))