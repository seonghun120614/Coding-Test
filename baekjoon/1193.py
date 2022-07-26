import math

x = int(input())
n = math.ceil(math.sqrt(2*x + 0.25) - 0.5)
    
if n%2 == 0 :
    q = int(x-(n-1)*n/2)
    p = int(n+1-q)
else :
    p = int(x-(n-1)*n/2)
    q = int(n+1-p)

print(str(q)+'/'+str(p))