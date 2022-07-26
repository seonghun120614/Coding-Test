# BFS 너비 우선 탐색
# deque 필요

graph = [
    1:set([3,4]),
    2:set([3,4,5]),
    3:set([1,5]),
    4:set([1,4,5]),
    5:set([3,5]),
    6:set([3,4,7],
    [7],
    [2,6,8],
    [1,7]
]

from collections import deque

def BFS_with_adj_lst(graph, root) :
    visited = []
    queue = deque([root])
    
    while queue :
        n = queue.popleft()
        if n not in visited :
            visited.append(n)
            queue += graph[n] - set(visited)
    
    return visited

print(BFS_with_adj_lst(graph, 0))