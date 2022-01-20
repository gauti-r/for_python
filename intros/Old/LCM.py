lis=input("Give two numbers to find their LCM :").split(" ")
a=int(lis[0])
print(a)

b=int(lis[1])
print(b)

for i in range(1,a*b+1):
    if(i%a==0)and (i%b==0):
        print("The LCM is ",i)
        break


