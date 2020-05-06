
s=0
for i in range(1,1001):
    s+=pow(i,i)
print(s)

L=list(str(s))
c= -10
x=[]

for i in range(0,10):
    x.append(L[c])
    c+=1
x="".join(x)
print(x)