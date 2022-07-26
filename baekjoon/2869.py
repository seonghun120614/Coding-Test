from sys import stdin
a, b, v = list(map(int, input().split()))
v, a = v-b, a-b
print(v//a + (v%a!=0))