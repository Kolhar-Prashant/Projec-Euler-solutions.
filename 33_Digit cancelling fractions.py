def remove_rep_digit(L):
    x = []
    rep_digit=0
    c=1
    for i in L:
        if i in x:

            rep_digit=i
            c+=1
        else:
            x.append(i)

    for _ in range(c):
        try:
            L.remove(rep_digit)
        except:
            print("Number not in list")
    return L

curious_fraction=[]

for a in range(1,100):
    for b in range(10,100):

        if b % 10 != 0:

            L=[]
            num_list=[]
            deno_list=[]

            #print(a,b)
            num_unit=a%10
            num_tens=a//10

            deno_unit = b % 10
            deno_tens = b // 10

            num_list.append(num_tens)
            num_list.append(num_unit)

            deno_list.append(deno_tens)
            deno_list.append(deno_unit)

            if num_unit in deno_list:

                L.append(num_tens)
                L.append(num_unit)
                L.append(deno_tens)
                L.append(deno_unit)

                if a != b:
                    try:
                        #print(L)
                        div1=a/b
                        #print(div1)

                        L=remove_rep_digit(L)
                        #print(L)
                        x=L[0]
                        y=L[1]
                        div2=x/y
                        #print(div2)
                        if div1 == div2 and div1 < 1:
                            temp=[]
                            print(div1, a,b)
                            temp.append(a)
                            temp.append(b)
                            print(div2, x, y)
                            print("--------------------")
                            curious_fraction.append(temp)

                    except:
                        print("Division by 0 !")

print(curious_fraction)

