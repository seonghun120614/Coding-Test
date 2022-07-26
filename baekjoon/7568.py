from sys import stdin

table = []
for i in "55 185\n58 188".split("\n") :
    table.append(tuple(map(int, i.split())))

for w, h in table :
    print(1+sum([w<i and h<j for i, j in table]), end=" ")