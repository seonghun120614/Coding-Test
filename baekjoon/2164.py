from sys import stdin
from collections import deque

deq = deque(range(1, int(input())+1))

i = deq.popleft()
while deq :
    deq.rotate(-1)
    i = deq.popleft()

print(i)