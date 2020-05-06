
def check_prime(n):
    for i in range(2,n):
        if n%i != 0:
            F=0
        else:
            F=1
            break
    return F

if __name__ == "__main__":

    n=3
    cnt=1
    rank=10001
    print("Started...")
    while (cnt != rank):
        
        F=check_prime(n)
        if F == 0:
            cnt+=1
            if cnt == rank:
                print("Number ",str(n),"is",str(cnt),"prime number in list")
        n+=1
    
