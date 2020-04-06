n=int(input("enter the number:"))
sum=0
for i in range(1,n):
    if(n%i==0):
        sum+=i
print(n,"is perfect number") if(sum==n) else print(n,"  is not perfect")
