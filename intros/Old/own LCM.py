#lcm of two numbers

lis=input("Give two numbers to find their LCM :").split(" ")
a=int(lis[0])
print(a)

b=int(lis[1])
print(b)

for i in range (1,20):
    for j in range (0,i+1):
        q=a*i
        r=b*j
        if(q==r):
            print("The LCM of the numbers ",a," & ",b," is ",r)
            break
