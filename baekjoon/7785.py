from sys import stdin

input = stdin.readline

def solution():
    res = dict()
    for _ in range(int(input())) :
        name, status = input().split()
        
        if status[0] == "l" and name in res : del res[name]
        else : res[name] = 1
    
    print(*sorted(res.keys(), reverse=True), sep = "\n")

solution()