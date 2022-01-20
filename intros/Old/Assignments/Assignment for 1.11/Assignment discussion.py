#check prime

def check_prime(num):
    for i in range(2,num//2+1):
        if num%i==0:
            return False
    return True

num = int(input("enter the number :"))

print("The input " +str(num)+ "is prime: " +str(check_prime(num)))
f"The input {num}  is prime : {check_prime(num)}"

#2

def check_prime(num):
    for i in range(2,(num//2)+1):
        print(i)
        if num%i==0:
            return False
    return True

def all_primes(num):
    primes=[]
    for i in range(2,num+1):
        print(i)
        if check_prime(i):
            primes.append(i)

    return primes

def soe(num):
    primes = [True for i in range(2,num+1)]
    p=2
    while p**2 < num:
        if primes[p-2]:
            for i in range(p**2,num+1):
                primes[i-2]= False


if __name__=="__main__":
    num = int(input("Enter the number: "))
    print(all_primes(num))


#3.1

def binary_search_recurse(slist,num):
    if num<slist[0] or num>slist[-1]:
        return "Not Found. "
    mid=slist[int(len(slist)//2)]
    if num ==mid:
        return "Number found!"
    elif num>mid:
        return binary_search_recurse(slist[mid + 1:], num)
    else:
        return binary_search_recurse(slist[:mid],num)
sorted_list = [2,3,4,5,6,7,8,9,10]
num=int(input("Number to search: "))
print(binary_search_recurse(sorted_list,num))

#3.2 binary search with loop

def binary_search_loop(slist,num):
    result="not found."
    while len(slist)>0:
        mid=int(len(slist)//2)
        if num ==slist[mid]:
            result="found."
            break
        elif num>slist[mid]:
            slist=slist[mid+1:]
        else:
            slist=slist[:mid]
    return result

#4 Selection Sort

def selection_sort(ulist):
    for i in range(len(ulist)):
        min_idx=1
        for j in range(i+1, len(ulist)):
            if ulist[j] < ulist[min_idx]:
                min_idx=j
        ulist[i],ulist[min_idx]=ulist[min_idx],ulist[i]
    return ulist

ulist=[8,5,6,9,7,1,3,4,2]
print(selection_sort(ulist))

#5 Bubble Sort

def bubble_sort(ulist):
    for i in range(len(ulist)):
        for j in range((len(ulist))-i-1):
            if ulist[j]>ulist[j+1]:
                ulist[j],ulist[j+1] = ulist[j+1],ulist[j]
    return ulist

ulist = [8, 5, 6, 9, 7, 1, 3, 4, 2]
print(bubbble_sort(ulist))

#5 Merge Sort