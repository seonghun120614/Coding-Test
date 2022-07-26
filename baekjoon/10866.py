from sys import stdin
from collections import deque

def solution() :
    deq = deque()
    _, *lst = stdin.readlines()
    l = 0
    for i in lst : 
        try :
            if i[0] == "s" :
                print(l)
            elif i[0] == "b" :
                print(deq[-1])
            elif i[0] == "e" :
                print(int(l==0))
            elif i[0] == "p" :
                if i[1] == "u" :
                    if i[5] == "f" :
                        deq.appendleft(int(i.split()[-1]))
                    else :
                        deq.append(int(i.split()[-1]))
                    l += 1
                else :
                    if i[4] == "f" :
                        print(deq.popleft())
                    else :
                        print(deq.pop())
                    l -= 1 * (l!=0)
            else :
                print(deq[0])
        except :
            print(-1)
            
solution()