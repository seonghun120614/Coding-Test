from sys import stdin

input = stdin.readline
n, k = int(input()), int(input())
lst = input().split()

if n>=k :
    print(*sorted([int(_) for _ in set(lst)]))
else : 
    
    dict1 = dict()
    
    for idx, recommend in enumerate(lst) :
        
        if recommend in dict1 :
            dict1[recommend][0] += 1
        else :
            if len(dict1) == n :
                
                # 횟수, 사진틀에 들어온 순서의 value중 최소인 것의 key를 구해서 없애기
                del dict1[min(dict1.keys(), key=lambda x: (dict1[x][0], dict1[x][1]))]
            
            # 추가하기
            dict1[recommend] = [1, idx]

    res = sorted([int(_) for _ in dict1.keys()])
    print(*res)
