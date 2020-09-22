
def check(n):
    for multipler in range(2,7):
        m = n * multipler
        for e in str(m):
            if e not in str(n):
                return 0
    perm_mul.append(n)

perm_mul = []
for num in range(2,1000000):
    check(num)
print("Number to contain all the permutations of digits in it's multiples from 2x to 6x is :",perm_mul)