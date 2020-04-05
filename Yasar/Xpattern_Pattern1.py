n=int(input("Enter no.of.rows"))
#for rows
for i in range(0,n):
       for j in range(0,n): #for columns
              
              if(i==j) or n-1==j+i or i==0 or i==n-1 or j==0 or j==n-1:
                     print("*",end=" ")
              else:
                     print(" ",end=" ")

       print()



   
"""n=rows"
n-1=last row==i"""
