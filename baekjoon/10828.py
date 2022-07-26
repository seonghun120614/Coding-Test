from sys import stdin
from collections import deque

lst = deque()

def solution(s1, lst) :
    if "pu" == s1[:2] :
        lst.append(int(s1.split()[-1]))
    
    elif "to" == s1[:2] :
        if not lst : print(-1)
        else : print(lst[-1])
    
    elif "po" == s1[:2] :
        if not lst : print(-1)
        else : print(lst.pop())

    elif "s" == s1[0]:
        print(len(lst))

    else:
        print(int(not lst))


for _ in range(int(input())) :
    solution(stdin.readline(), lst)