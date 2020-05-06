def check(n):
    F = 0
    for e in Pen:
        if n == e:
            F = 1
            break
    F1 = 0
    for e in Hex:
        if n == e:
            F1 = 1
            break

    if F == 1 and F1 == 1:
        print("Number present in All", e)

def gen_Triangular(Limit):

    for n in range(1,Limit):
        t = n * (n + 1) // 2
        Tri.append(t)

def gen_Pentagonal(Limit):

    for n in range(1,Limit):
        t = n * (3*n - 1) // 2
        Pen.append(t)

def gen_Hexagonal(Limit):

    for n in range(1,Limit):
        t = n * (2*n - 1)
        Hex.append(t)

Tri=[]
Pen = []
Hex=[]

Limit=1000000

gen_Triangular(Limit)
gen_Pentagonal(Limit)
gen_Hexagonal(Limit)

for e in Tri:
    check(e)