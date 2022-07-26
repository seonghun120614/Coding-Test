a, b, c = list(map(int, input().split()))
unit_benifit = c-b
if unit_benifit<=0 :
    print(-1)
else :
    print(a//(c-b)+1)