
def star(n) :
    res = ""
    for i in range(n,0,-1) : res+= "*"*i + "\n"
    print(res)

star(int(input()))