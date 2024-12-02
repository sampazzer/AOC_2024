#Test input
test_input= """ 3   4
4   3
2   5
1   3
3   9
3   3
"""

p1 = []
p2 = []
r = []
with open("input.txt") as f:
    fa = f.read().splitlines()


for a in fa:
    b = a.replace(" ","")
    p1.append(int(b[0:5]))
    p2.append(int(b[5:10]))

p1.sort()
p2.sort()

for a in p1:
    c=0
    for b in p2:
        if a == b:
            c+=1
    r.append(c*a)

rs = sum(r)

print(rs)
