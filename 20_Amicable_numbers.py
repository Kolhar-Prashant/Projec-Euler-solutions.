
def sum_of_proper_divisor(n):
    sum=0
    x=[]
    lim= (n//2)+1       #optimizing the loop by checking divisiors till half + 1
    for i in range(1,lim):
        if n % i == 0:
            sum+=i
            x.append(i)
    if n != sum:
        return sum
    else:
        return -1

if __name__ == "__main__":

    sum=0
    memo=[]
    for n in range(10000):  #put limit value here.
        if n not in memo:           # using memoziation concept to skip calculations on a amicable pair.
            #print(n)
            x = sum_of_proper_divisor(n)
            if x != -1:
                y = sum_of_proper_divisor(x)
            else:
                continue
            if y == n:
                sum += n
                sum += x
                memo.append(x)
    print("sum of amicable numbers from 1 to 10000", str(sum))