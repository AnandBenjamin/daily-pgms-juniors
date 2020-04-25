#program to find collatz conjecture for a given number
"""
from the given number,it gradually decrease to 1 based on odd or even of the number
"""


n=int(input())

while n>1:
       
   print(n,end=" ")
   if n%2==0:
       n=n//2
      
   else:
       n=3*n+1
print(1,end=" ")
       

"""def collatz(n):
    while n > 1:
        print(n, end=' ')
        if (n % 2):
            # n is odd
            n = 3*n + 1
        else:
            # n is even
            n = n//2
    print(1, end='')
 
 
n = int(input('Enter n: '))
print('Sequence: ', end='')
collatz(n)
"""
