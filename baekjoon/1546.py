from sys import stdin

input = stdin.readline

n = int(input())
l = list(map(int, input().split()))
m = max(l)
print(sum(l)/m*100/n)
