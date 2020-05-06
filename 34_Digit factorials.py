
def factorial(num):
    d={0:1,1:1,2:2,3:6,4:24,5:120,6:720,7:5040,8:40320,9:362880}

    for k in d.keys():

        if k == num:
            return d[k]

total_sum=0
for num in range(13,50000):
    sum = 0
    n=str(num)

    for e in n:

        x=factorial(int(e))
        sum+=x

    if num == sum:
        total_sum+=num
        print("Curous number",str(num))

print("Total sum",str(total_sum))
