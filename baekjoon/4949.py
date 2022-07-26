from sys import stdin

def solution(s) :
    lst = []
    
    for i in s :
        if i in "()[]" :
            if i in "([" :
                lst.append(i)
            else :
                try :
                    if i == "]" :
                        if lst[-1] == "[" :
                            lst.pop()
                        else :
                            return "no"
                    else :
                        if lst[-1] == '(' :
                            lst.pop()
                        else :
                            return "no"
                except :
                    return "no"
                    
        
    if lst : return 'no'
    else : return 'yes'

lines = stdin.readlines()

print("\n".join(list(map(solution, lines[:-1]))))