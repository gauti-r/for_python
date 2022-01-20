n=int(input("Give a number : "))

print(n)
i=1
j=10
while(i>0):
    if(n<j):
        print ("It is a ",i," digit number")
        break
    else:
        j=j*10
        i=i+1
    
   
