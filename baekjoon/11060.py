from sys import stdin

input = stdin.readline

n = int(input())
lst = list(map(int, input().split()))
tmp = [1001]*n
tmp[0] = 0

for i in range(n-1) :
    for j in range(i+1, i+lst[i]+1) :
        try :
            tmp[j] = min(tmp[j], tmp[i]+1)
        except :
            pass

print(tmp[-1] if tmp[-1]!=1001 else -1)