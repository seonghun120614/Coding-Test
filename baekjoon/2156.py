from sys import stdin

n, *lst = list(map(int, stdin.readlines()))

cost = [0, 0]
now, res = 0, 0

while now < n-2 :
    cost[0] = lst[now] + lst[now+2]
    cost[1] = lst[now] + lst[now+1]
    
    arg = max(range(2), key=lambda x : cost[x])
    
    if arg==0 : res += lst[0]
    else : res += lst[0] + lst[1]
    
    now += 2+arg

print(res)