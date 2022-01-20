# 1 Check if Prime Number

def check_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print("The input is not a prime number")
                break
            else:
                print("The input is a prime number")
                break
    else:
        print("The input is not a prime number")

# 2 find and print prime numbers : sieve of erasthoneses

def find_primes(num):
    list=[]
    prime = [True for i in range(num + 1)]
    p = 2
    while (p * p <= num):
        if (prime[p] == True):
            for i in range(p * 2, num + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    for p in range(num + 1):
        if prime[p]:
            list.append(p)
    print("The prime numbers before the given number are : ",list)

#3.1 Recursive Binary Search (Not Working)

value = int(input("Give a value to search for: "))
mylist = list(input("Give a sorted list : "))
def binary_search_recurse(mylist,value,low=0,mid=0):
    high = len(mylist)
    if high >= low:
        mid = (high + low) // 2
        if int(mylist[mid]) == value:
            return mid
        elif int(mylist[mid]) > value:
            return binary_search_recurse(mylist, value, low, mid - 1)
        else:
            return binary_search_recurse(mylist, value, mid + 1, high)
    else:
        return -1

result = binary_search_recurse(mylist,value, 0, len(mylist) - 1)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")

#5.2 Iterative binary search

def binary_search(mylist=[], value=0):
    value = int(input("Give a value to search for: "))
    mylist = list(input("Give a sorted list : "))
    low = 0
    high = len(mylist) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        if int(mylist[mid]) < int(value):
            low = mid + 1

        elif int(mylist[mid]) > int(value):
            high = mid - 1

        else:
            return mid
    return -1
result = binary_search(mylist, value)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")


#4 Selection Sort

def selection_sort(mylist=0):
    import sys
    mylist = list(input("Enter the list of unsrted numbers : "))
    for i in range(len(mylist)):
        min_idx = i
        for j in range(i + 1, len(mylist)):
            if mylist[min_idx] > mylist[j]:
             min_idx = j
        mylist[i], mylist[min_idx] = mylist[min_idx], mylist[i]
    b = []
    print("Sorted array")
    for i in range(len(mylist)):
        b.append(mylist[i])

    print(b)

#5 Bubble sort

def bubble_sort(mylist=0):
    mylist = list(input("Enter the list of unsrted numbers : "))
    n = len(mylist)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if mylist[j] > mylist[j + 1]:
                mylist[j], mylist[j + 1] = mylist[j + 1], mylist[j]
    b = []
    print("Sorted array")
    for i in range(len(mylist)):
        b.append(mylist[i])
    print(b)





