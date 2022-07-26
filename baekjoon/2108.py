from sys import stdin
from collections import Counter

n, lst = int(input()), sorted(list(map(int, stdin.readlines())))
# n = 7
# lst = [1,1,1,2,3,4,5]
if n>1 :
    cnt = Counter(lst).most_common(2)
    print(round(sum(lst)/n))
    print(lst[int((n-1)/2)])
    if cnt[0][1] == cnt[1][1] :
        print(int(cnt[1][0]))
    else :
        print(int(cnt[0][0]))
    print(max(lst) - min(lst))
else :
    print(lst[0], lst[0], lst[0], 0, sep='\n')