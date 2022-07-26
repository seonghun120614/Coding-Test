from collections import deque
from sys import stdin

input = stdin.readline

def bfs(node):
    deq = deque()
    deq.append(node)
    while deq:
        node = deq.popleft()
        for n in graph[node]:
            if chk[n] == 0:
                chk[n] = chk[node]+1
                deq.append(n)


n = int(input())
graph = [[] for _ in range(n+1)]
p1, p2 = map(int, input().split())

for _ in range(int(input())):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
chk = [0]*(n+1)
bfs(p1)
print(chk[p2] if chk[p2] > 0 else -1)