
limit=100
sum_sqr=0
for i in range(1,limit+1):
    sum_sqr+=i*i
#print(sum_sqr)

sum=0
for i in range(1,limit+1):
    sum+=i
sqr_sum=sum*sum
#print(sqr_sum)

diff=sqr_sum-sum_sqr

print("Difference between sum of sqaures and square of sums :",str(diff))