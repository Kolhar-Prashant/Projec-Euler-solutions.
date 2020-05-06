
def split_num(num):
    sum=0
    for e in num:

        e=int(e)
        n=e ** 5
        sum+=n

    if int(sum) == int(num):
        print("Number is sum of fifth powers of their digits:", num)
        L.append(num)

if __name__ == "__main__":

    L=[]
    for s in range(1,1000000):

        n=str(s)
        split_num(n)

    x=0
    for i in L:

        x+=int(i)
    print("Summation : ", x)
