a=1
b=2
#print(a)
#print(b)
sum=2
limit=4000000
for i in range(limit):
    
    temp=a+b
    #print(temp)
    if temp >=limit:
        break
    if temp%2==0:
        #print(temp)
        sum+=temp
    b=temp 
    a=b-a

print("Summation of even valued fibo numbers : ", str(sum))
    
