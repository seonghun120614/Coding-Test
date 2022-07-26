from sys import stdin

input = stdin.readline

def solution(order_lst) :
    lst = []
    for i in order_lst :
        if i == 0 :
            if len(lst) > 0 :
                lst.pop()
        else :
            lst.append(i)
    print(sum(lst))

solution([int(input()) for _ in range(int(input()))])