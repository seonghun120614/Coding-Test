from sys import stdin
from collections import Counter

def solution() :
    _, *lst = stdin.readlines()
    lst = Counter(lst)
    return sorted(lst.most_common(), key = lambda x : (-x[1], x[0]))[0][0].rstrip()
    
print(solution())