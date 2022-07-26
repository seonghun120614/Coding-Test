from itertools import permutations

n, m = list(map(int, input().split()))
res = ""

for i in permutations(range(1, n+1), r=m) : print(*i)