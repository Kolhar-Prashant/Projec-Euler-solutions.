
def power(n):
    for i in range(2,101):
        pow=n**i
        L.append(pow)

if __name__ == "__main__":
    L=[]

    for i in range(2,101):
        power(i)

    L=list(set(L))
    L.sort()
    print(len(L))