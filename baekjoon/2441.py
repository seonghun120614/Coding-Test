
def star(n) :
    res = ""
    for i in range(n,0,-1) : res+= " "*(n-i) + "*"*i + "\n"
    print(res)

star(int(input()))