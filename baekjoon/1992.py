from sys import stdin

input = stdin.readline

n = int(input())
s = [input().rstrip() for _ in range(n)]

def divide(s, n) :
    d = n//2
    lf, rf, lb, rb = [],[],[],[]
    for i in s[:d] : 
        lf.append(i[:d])
        rf.append(i[d:])
    for i in s[d:] : 
        lb.append(i[:d])
        rb.append(i[d:])
    
    return lf, rf, lb, rb

def conquer(s, n) :
    s_tmp = set()
    for i in s : s_tmp = s_tmp.union(i)
    res = ""
    if len(s_tmp) == 1 :
        if "1" in s_tmp : res+="1"
        else : res+="0"
        return res
    if n==2 : return "("+"".join(s)+")"
    else :
        tmp = n//2
        res += "("
        for i in divide(s, n) :
            res += conquer(i, tmp)
        res += ")"
        return res
    
print(conquer(s, n))