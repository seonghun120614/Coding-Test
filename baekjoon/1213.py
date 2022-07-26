from collections import Counter, deque

def solution(s) :
    
    c = Counter(s)
    mid = list(filter(lambda x:x[1]%2!=0, c.items()))
    
    if len(mid)>1 :
        print("I'm Sorry Hansoo")
        
    else :
        try :
            res = deque(mid[0][0])
            c[mid[0][0]] -= 1
        except :
            res = deque()
        finally :
            for i in sorted(c, reverse=True) :
                tmp = i*(c[i]//2)
                res.extend(tmp)
                res.extendleft(tmp)
            print(*res, sep="")

solution(input())
