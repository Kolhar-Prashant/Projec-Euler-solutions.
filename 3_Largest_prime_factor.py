F=[]
n=600851475143
r=0
d=2
f=0
while f != 1:

    f=n/d   
    r=n%d 
    if r == 0:
        n=f
        F.append(d)
    else:
        d+=1    
print("Largest Prime factor : ",str(F[-1]))
