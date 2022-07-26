from sys import stdin
import math

input = stdin.readline
n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

def solution(lst, n) :
    white = 0
    blue = 0
    
    for i in range(int(math.log2(n)), -1 , -1) :
        tmp = 2**i
        for j in range(0, n, tmp):
            for k in range(0, n, tmp):
            
                if lst[j][k]==-1 : continue
                chk = True
                s=set()
                for l in range(tmp) :
                    s = s.union(lst[j+l][k:k+tmp])
                    if len(s)>1 :
                        chk = False
                        break

                if chk :
                    for l in range(tmp) : lst[j+l][k:k+tmp] = [-1]*tmp
                    if 0 in s : white+=1
                    else : blue+=1
        
    print(white, blue, sep="\n")


solution(lst, n)