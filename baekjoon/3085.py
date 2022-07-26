from sys import stdin

input = stdin.readline

def cnt(s) :
    tmp = 1
    m = 0
    for i in range(1, n) :
        if s[i-1] == s[i] : tmp += 1
        else :
            m = max(tmp, m)
            tmp = 1
            
    m = max(tmp, m)
    return m


def row(lst, k) :
    return [lst[i][k] for i in range(n)]


def solution() :
    m = 0

    for i in range(n-1) :
        for j in range(n) :
            chk = lst[i][j] != lst[i+1][j]
            if chk :
                lst[i][j], lst[i+1][j] = lst[i+1][j], lst[i][j]
                for k in range(n) :
                    m = max(cnt(lst[k]), m)
                    m = max(cnt(row(lst, k)), m)
                lst[i][j], lst[i+1][j] = lst[i+1][j], lst[i][j]
            
    for i in range(n) :
        for j in range(n-1) :
            chk = lst[i][j] != lst[i][j+1]
            if chk :
                lst[i][j], lst[i][j+1] = lst[i][j+1], lst[i][j]
                for k in range(n) :
                    m = max(cnt(lst[k]), m)
                    m = max(cnt(row(lst, k)), m)
                lst[i][j], lst[i][j+1] = lst[i][j+1], lst[i][j]

    print(m)

n = int(input())
lst = [list(input().rstrip()) for _ in range(n) ]

solution()


