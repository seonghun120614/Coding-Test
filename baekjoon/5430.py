from sys import stdin

def solve(s, n, lst):
    pos1, pos2 = 0, n
    j = True
    D_cnt = s.count("D")
    
    if D_cnt > n or s=="" :
        return "error"
    
    elif D_cnt == n :
        if s[-1] == "R" :
            return "error"
        else :
            return []
    
    else :
        str_lst = s.split("R")
        for i in str_lst:
            if j : pos1 += len(i)
            else : pos2 -= len(i)
            j = not j
        if j : return "["+",".join(list(reversed(lst[pos1:pos2])))+"]"
        return "["+",".join(lst[pos1:pos2])+"]"

for _ in range(int(input())) :
    s = stdin.readline().strip()
    n = int(stdin.readline())
    lst = stdin.readline().strip("[]\n")
    
    if lst == "" :
        lst = []
    else :
        lst = lst.split(",")

    print(solve(s, n, lst))
