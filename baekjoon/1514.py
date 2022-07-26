from sys import stdin
from collections import deque

n, *wine = list(map(int, stdin.readlines()))
d = deque(maxlen=3)

try :
    d.extend([wine[0], wine[0] + wine[1]])
    d.append(max(wine[2]+wine[0], wine[1]+wine[2], d[1]))

    for i in range(3, n) :
        d.append(max(wine[i]+d[1], wine[i]+wine[i-1]+d[0], d[2]))
    print(d.pop())
except :
    print(sum(wine))