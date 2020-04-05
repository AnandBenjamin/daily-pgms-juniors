def numpattern(n):
    num=1
    for i in range(0,n):
        num=1                             #reassign num here to increment from one itself
        for j in range(0,i+1):            
            print(num,end=" ")
            num+=1
        print()
#n=int(input())
n=5
numpattern(n)

"""to handle the row the first for loop is used

to handle column inner for loop is used"""
