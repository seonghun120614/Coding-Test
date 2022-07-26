from sys import stdin

_ = input()
lst = list(map(int, stdin.readlines()))

lst.sort()
for i in lst :
    print(i)
