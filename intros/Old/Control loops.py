q=int(input("Give no of iteration : "))
while (q>0):
    for i in range(1,10):
        for j in range(1,i):
            print("*",end=("$"))
        print("")

    for a in range(1,10):
        for b in range (1,10-a):
            print ("*",end='$')
        print("")
    q=q-1
    continue
    
