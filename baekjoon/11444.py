from functools import reduce

def power(n) :
    if n<=1 :
        b = n==1
        return [[1,int(b)],[int(b),int(not b)]]
    else:
        tmp = power(n//2)
        
        if n%2 == 1 :
            return reduce(mat_mul_div, [
                tmp,
                tmp,
                [[1,1],[1,0]]
            ])
        else :
            return mat_mul_div(tmp, tmp)

# 행렬곱 연산 수행
# 수행 도중 합동식을 통한 1000000007로 나눔
def mat_mul_div(lst1, lst2) :
    d = int(1e9 + 7)
    f1 = (lst1[0][0]*lst2[0][0] + lst1[0][1]*lst2[1][0])%d
    f2 = (lst1[0][0]*lst2[0][1] + lst1[0][1]*lst2[1][1])%d
    f3 = (lst1[1][0]*lst2[0][1] + lst1[1][1]*lst2[1][1])%d
    
    return [[f1, f2],[f2, f3]]

if __name__ == "__main__" :
    d = int(1e9 + 7)
    n = int(input())-1
    lst = []
    print(power(n)[0][0])