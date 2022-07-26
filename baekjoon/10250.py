from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    h, w, n = list(map(int, input().split()))
    
    if h!=1 and w!=1 :
        num_100 = n%h
        num = n//h+1 - (num_100==0)
        if num_100 == 0 : num_100 = h
    else :
        if h==1 : num_100, num = 1, n
        else : num_100, num = n, 1
            
    print(num_100*100 + num)