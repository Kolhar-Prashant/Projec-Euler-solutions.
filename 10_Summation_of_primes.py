import datetime

def check_prime(n):
    F=0
    for i in range(2,n-1):
        if n % i == 0:
            F=-1
            return F
    return F

if __name__ == "__main__":

    a = datetime.datetime.now()
    limit=100000
    x=[]
    for n in range(2,limit):
        #print(n)
        F=0
        F=check_prime(n)

        if F == 0:
            x.append(n)
    print(x)

    b = datetime.datetime.now()
    c = b - a
    print(c.microseconds)