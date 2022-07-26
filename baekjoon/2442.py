def star(n) :
    res = ""
    for i in range(n-1, -1, -1) : 
        txt = " "*(n-i-1)
        res += txt + "*" + "*"*(i*2)+ "\n"
    print(res.rstrip())

star(int(input()))