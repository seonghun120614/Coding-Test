
croatia_set = ('c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=')

def solve(str) :
    res = 0
    for i in croatia_set :
        if str.find(i):
            res += 1
    
    return res

print(solve(input()))