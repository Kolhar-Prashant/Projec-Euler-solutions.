
def sum(x,a,s):

    x+=a
    #print(x)
    L.append(x)
    a+=8
    s+=x
    return x,a,s

if __name__ == "__main__":
    a=8
    x=1
    L=[]
    summ1=0
    limit=7
    #limit = (limit-1)//2
    for i in range(limit):
        x,a,summ1=sum(x,a,summ1)

    #print(summ1)
    
    a = 4
    x = 1
    summ2 = 0
    for i in range(limit):
        x, a, summ2 = sum(x, a, summ2)

    #print(summ2)


    a = 6
    x = 1
    summ3 = 0
    for i in range(limit):
        x, a, summ3 = sum(x, a, summ3)

    #print(summ3)
    
    a = 2
    x = 1
    summ4 = 0
    for i in range(limit):
        x, a, summ4 = sum(x, a, summ4)

    #print(summ1+summ2+summ3+summ4+1)
    L.sort()
    ss=1
    print(L)
    for i in L:
        ss+=i
    print(ss)