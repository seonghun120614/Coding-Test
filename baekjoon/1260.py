from sys import stdin
input = stdin.readline

n, m, v = list(map(int, input()))

def solution(n, m, v) :
    graph = {i:[] for i in range(1, n+1)}
    start, end = list(map(int, input().split()))
    