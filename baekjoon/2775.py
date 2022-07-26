from sys import stdin
import math
input = stdin.readline

def combination(n, r) :
    return int(math.factorial(n)/(math.factorial(r) * math.factorial(n-r)))

for _ in range(int(input())) :
    floor, num = int(input()), int(input())
    print(combination(floor+num, num-1))