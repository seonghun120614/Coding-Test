def solving(n, k) :
    lst = [_ for _ in range(2, n+1)]
    res = 0
    for i in lst :
        res+=1
        if res==k : return 1*i
        for j in range(2, n//i+1) :
            try :
                lst.remove(j*i)
                res+=1
                if res==k : return j*i
            except :
                pass

n, k = list(map(int, input().split()))
print(solving(n, k))