num = int(input())
sum = 0
temp=num
c=len(str(num))
for i in range (temp):
        d= temp% 10
        sum += d ** c
        temp //= 10# display the result
if num == sum:
    print("amstrong")
else:
    print("not a amstrong")


"""
n = int(input())
for i in range(1,n + 1):
    sum = 0
    temp = i
    length=0
    while temp>0:
        length+=1
        temp//=10
    temp=i
    while temp > 0:
        digit = temp % 10
        #print(digit)
        sum += digit ** length
        temp //= 10
        #print(temp)
    if i == sum:
        print(i)
"""
