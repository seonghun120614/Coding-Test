from sys import stdin

n, *lst = stdin.readlines()

def solution(n, llst) :
    tmp = 1
    rng = [1]
    res = "+"
    for i in llst :
        while True:
            if tmp > n : return "NO"
            if rng and rng[-1] == i :
                rng.pop()
                res += "\n-"
                break
            else :
                res += "\n+"
                tmp += 1
                rng.append(tmp)

    return res
    

print(solution(int(n), [int(i) for i in lst]))