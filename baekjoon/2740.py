from sys import stdin

input = stdin.readline

def product_sum(v1, v2) :
    res = 0
    for i, j in zip(v1, v2) : res += i*j
    return res

n, m = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(n)]
m, k = list(map(int, input().split()))
b = [list(map(int, input().split())) for _ in range(m)]
c = []
for i in range(n) :
    tmp = []
    for j in range(k) :
        tmp.append(product_sum(a[i], [_[j] for _ in b]))
    c.append(tmp)

for i in c :
    print(*i)