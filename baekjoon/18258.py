from sys import stdin
from collections import deque

input = stdin.readline
res = deque()

for _ in range(int(input())) :
    i = input()
    try :
        if i[0] == "f" :
            print(res[0])
        elif i[0] == "b" :
            print(res[-1])
        elif i[0] == 's' :
            print(len(res))
        elif i[0] == 'e' :
            print(int(not bool(res)))
        else :
            if i[1] == 'u' :
                res.append(int(i.split()[-1]))
            else :
                print(res.popleft())
    except :
        print(-1)
