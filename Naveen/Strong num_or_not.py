num=int(input())
t=num
sum=0
while(t!=0):
    fact=1
    i=1
    rem=t%10
    while(i<=rem):
        fact*=i
        i+=1
    sum=sum+fact
    t//=10
if(num==sum):
    print("strong number")
else:
    print("Not a strong")
