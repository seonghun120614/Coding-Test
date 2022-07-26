import sys
input = sys.stdin.readline


n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
paper = [0, 0, 0]


def divide(n) :
    d = n//3
    return [(i, j) for i in range(0, n, d) for j in range(0, n, d)]


def conquer(pos, n) :
    s = set()
    d = n//3
    
    if n==3 :
        tmp = [0, 0, 0]
        for i in range(3) :
            for j in range(3) :
                tmp[lst[pos[0]+i][pos[1]+j]] += 1
        
        for i in range(-1, 2) :
            paper[i] += tmp[i]%9 + (tmp[i]==9)
        return
        
    else :
        for i in range(n) :
            s = s.union(lst[i])
            if len(s) > 1 :
                for j in divide(n) :
                    conquer(j, d)
                return
        paper[tuple(s)[0]] += 1
        return

conquer((0,0), n)
print(paper[-1], paper[0], paper[1], sep="\n")






import sys
input = sys.stdin.readline

def divide(pos, n) :
    step = n//3
    res = []
    for i in range(pos[0], pos[0]+n, step) :
        for j in range(pos[1], pos[1]+n, step) :
            res.append((i, j))
    return res

def conquer(pos, n) :
    s = set()
    tmp = True
    tmp1 = n//3
    
    for i in lst[pos[0]:pos[0]+n] : 
        s = s.union(i[pos[1]:pos[1]+n])
        
        if len(s) > 1 :
            if n==3 :
                for j in range(3) :
                    for k in range(3) : paper[lst[j+pos[0]][k+pos[1]]+1] += 1
            else : for k in divide(pos, n) : conquer(k, tmp1)
            return
        
    if tmp : paper[tuple(s)[0]+1] += 1

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
paper = [0, 0, 0]

if n==1 : paper[lst[0][0]+1] += 1
else : conquer((0,0), n)

print(*paper, sep="\n")