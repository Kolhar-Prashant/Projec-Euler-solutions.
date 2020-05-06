import re

def check(s,prod):
    L=[]
    c=0
    for e in s:
        if re.match(r'^\d{1}$',e):
            if e != '0':
                if e not in L:
                    L.append(e)
                    c+=1
                else:
                    return 0

    if c == 9:
        print(s, "Pandigital number")
        Prod_list.append(prod)


Prod_list=[]
L=[]

for i in range(1,10):  #1000
    for j in range(1,100):   #10000

        L.append(str(i))
        L.append(str(j))
        L.append(str(i*j))
        prod=i*j
        s=str(i)+str(j)+str(i*j)

        if len(s) == 9:
            L=str(L)
            check(L,prod)
            L=[]

sum=0
Prod_list=list(set(Prod_list))
#print(Prod_list)
for prods in Prod_list:
    sum+=prods

print("Product of all pandigit numbers",str(sum))