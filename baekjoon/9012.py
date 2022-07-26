from sys import stdin

input = stdin.readline

def solution(s) :
    lst = []
    
    for i in s :
        if i=="(" : lst.append("(")
        else :
            try : lst.pop()
            except : return "NO"
    
    if lst :
        return "NO"
    else :
        return "YES"

print("\n".join(list(map(solution, [input().rstrip() for _ in range(int(input()))]))))