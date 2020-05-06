a=1
b=1
F=3


while True:
    c=a+b
    x=str(c)
    if len(x) == 1000:
        print(F ," index is the first term to contain 1000 digits fibo number",x)
        break
    F+=1
    b=c
    a = b - a
