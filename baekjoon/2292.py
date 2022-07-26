import math

x = (int(input())-1)/6
n = math.ceil(math.sqrt(2*x + 0.25) - 0.5)+1
print(n)