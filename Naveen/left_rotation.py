def leftRotate(arr, d, n): 
	for i in range(d): 
		leftRotatebyOne(arr, n)

#loop for left rotating the ements 
def leftRotatebyOne(arr, n): 
	temp = arr[0] 
	for i in range(n-1): 
		arr[i] = arr[i + 1] 
	arr[n-1] = temp 
		
# func to print an array  
def printArray(arr, size): 
	for i in range(size): 
		print ("% d"% arr[i], end =" ")
n=int(input())
a = [int(i)for i in input().split()][:n] #array elements
arr=list(a) # storing them into list
d=int(input()) #rotation
leftRotate(arr,d,n) 
printArray(arr,n) 
