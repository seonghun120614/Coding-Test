from collections import deque

n, k = list(map(int, input().split()))

lst = deque(range(1, n+1))
res = []

while lst :
    lst.rotate(-(k-1))
    res.append(lst.popleft())
print("<", end="")
print(*res, sep=", ", end="")
print(">")