n, m = list(map(int, input().split()))

def is_primary(n) :
    if n==1 : return False
    i=2
    rng = n**0.5
    while i <= rng :
        if n%i==0 :
            return False
        i+=1
    return True

for i in range(n, m+1) :
    if is_primary(i) : print(i)


# m, n = map(int, input().split())
# li = [False] + [True] * ((n - 1) // 2)
# for x in range(1, int(n**.5/2+1)):
#   if li[x]:
#     li[2*x*(x+1)::x*2+1] = [False] * ((((n + 1) // 2) - x * x * 2) // (x * 2 + 1))
# if m <= 2:
#   print(2)
# print('\n'.join([f'{x}' for x, val in zip(range(m+(m&1==0), n+1, 2), li[m//2:]) if val]))