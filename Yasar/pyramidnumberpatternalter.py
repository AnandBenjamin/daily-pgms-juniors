n=int(input("Enter no .of.rows"))
for i in range(0,n):
    print((" "*(n-i-1))+(str(i+1)+' ')*(i+1))


#(" "*(n-i-1))if for spaces
#(str(i+1)+' ')for the number in each row
#i+1 for no.of.times
