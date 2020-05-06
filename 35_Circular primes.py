import math

def prime(sqr,lim):

    for e in range(2,sqr+1):
        for j in range(e,lim):
            prod=e*j
            if prod > lim:
                break
            else:
                L[prod]=False

    for e in range(2,len(L)):
        if L[e] == True:
            prime_List.append(e)

def check_prime(n):
    if n in prime_List:
        return 1
    return 0

def circulate(x):
    L = []
    L.extend(x[1:])
    L.append(x[0])
    L = "".join(L)
    x = L
    if L[0] == '0':
        L = int(L)
        if L in prime_List:
            return x
    return int(L)

prime_List=[]
lim=1000000
L=[True for i in range(lim+1)]
sqr=int(math.sqrt(lim))
prime(sqr,lim)

List = []
for num in range(2,lim):
#num = 101
    x = str(num)
    #print("str", x)
    Len = len(x)
    if Len == 1:
        if check_prime(num) == 1:
            List.append(num)
    else:
        temp_list = []
        c = 0
        for _ in range(Len):
            p = check_prime(num)
            if p == 1:
                c += 1
                temp_list.append(num)
                if c != Len:
                    num = str(num)
                    num = list(num)
                    num = circulate(num)
                else:
                    for e in temp_list:
                        List.append(e)
            else:
                temp_list = []
                break

List = list(set(List))
List=sorted(List)
print(List)
print(len(List))
