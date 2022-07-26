from collections import deque

s1, s2 = "1037265", "137297401073018286481862"
l1, l2 = len(s1), len(s2)

m = max(l1, l2)
a = abs(l1 - l2)

if l1 > l2 :
    s2 = "0" * a + s2
else :
    s1 = "0" * a + s1

j=False

dq_lst = deque()
for i in range(1,m+1):
    j, q = divmod(int(s1[-i]) + int(s2[-i]) + int(j), 10)
    dq_lst.appendleft(q)

if j : dq_lst.appendleft(1)

for _ in range(m + j) : print(dq_lst.popleft(), end="")