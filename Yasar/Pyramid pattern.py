"""def triangle(n): 
      
    # number of spaces 
    k = 10*n - 10 #k=10 specfiy it standardly
  
    # outer loop to handle number of rows 
    for i in range(0, n): 
      
        # inner loop to handle number spaces 
        # values changing acc. to requirement 
        for j in range(0, k): 
            print(end=" ") 
      
        # decrementing k after each loop 
        k = k - 1
      
        # inner loop to handle number of columns 
        # values changing acc. to outer loop 
        for j in range(0, i+1): 
          
            # printing stars 
            print("*", end=" ") 
      
        # ending line after each row 
        print("\r") 
  
# Driver Code 
n = 5
triangle(n)"""

def triangle(n): 
      
    # number of spaces 
    k = 1*n - 1 #k=10 specfiy it standardly
  
    # outer loop to handle number of rows 
    for i in range(0, n): 
      
        # inner loop to handle number spaces 
        # values changing acc. to requirement 
        for j in range(0, k): 
            print(end="*") 
      
        # decrementing k after each loop 
        k = k - 1
      
        # inner loop to handle number of columns 
        # values changing acc. to outer loop 
        for j in range(0, i+1): 
          
            # printing stars 
            print(i+1, end=" ")
                                                     
      
        # ending line after each row 
        print("\r") 
  
# Driver Code 
n = 5
triangle(n)





























