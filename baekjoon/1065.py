def han_num(n) :
    
    if n < 100 :
        return True
    
    else :
        s = str(n)
        c = list(map(int, s[:3]))
        if c[0]-c[1] != c[1]-c[2] : return False
        l, right = len(s), n%10
        dif = int("1"*l)*right
        
        n = n-dif
        l = len(s)-1
        div = sum([i*(10**i) for i in range(l)])
        
        return n%div==0

res = 0
for i in range(1, int(input()) +1) :
    if han_num(i) : res+=1

print(res)