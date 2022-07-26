from sys import stdout

def solution() :
    
    n, r1, c1, r2, c2 = list(map(int, input().split()))
    d = 2*n-1
    
    for i in range(r1, r2+1) :
        res = ""
        
        for j in range(c1, c2+1) :
            ctmp = abs((n-1)-j%d)
            rtmp = abs((n-1)-i%d)
            
            if ctmp >= n-rtmp : res+="."
            else : res+=chr(97+(rtmp+ctmp)%26)
            
        stdout.write(res+"\n")
    
solution()
