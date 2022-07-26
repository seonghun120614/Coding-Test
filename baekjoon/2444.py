def star_printing(n, align = "center") :
    # 변수 세팅
    left, right, center = False, False, False
    if align == "left" : left = True
    elif align == "right" : right = True
    else : center = True
    
    # 문자열 세팅
    left = " "*(n-i)*((left+center)*(1+left))
    center = "*"*(2*i + 1)
    right = " "*(n-i)*((right+center)*(1+right))

    # upper-star 출력
    for i in range(n-1) : print(left + center + right)
    # lower-star 출력
    for i in range(n-1, -1, -1) : print(left + center + right)
    
star_printing(5)