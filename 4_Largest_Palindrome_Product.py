def check_palindrome(n):
    f=0
    L=list(str(n))
    r=len(L)-1
    while (r-f > 0):
        if L[f] != L[r]:
            return -1
        else:
            f+=1
            r-=1
    return 0

prod=0
palindrome_list=[]

for i in range(100,1000):
    for j in range(100,1000):
        prod=i*j
        if prod > 100000: # optimization as a 2 three digit numbers product will be having 6 digits in minimum
            x=check_palindrome(prod)
            if x == 0:
                palindrome_list.append(prod)

palindrome_list=sorted(palindrome_list)
print("Largest Palindrome number:",palindrome_list[-1])