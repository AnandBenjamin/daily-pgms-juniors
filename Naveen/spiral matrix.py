def spiralPrint(m, n, a) : 
	k = 0#k - starting row index 
	l = 0#l - starting column index
	while (k < m and l < n) : #rowstart less thn row end..clm str less thn clm end		
		# Print the first row from the remaining rows 
		for i in range(l, n) : #clmn start to ending
			print(a[k][i], end = " ") #print app to tha elemet
			
		k += 1
		# Print the last column from the remaining columns 
		for i in range(k, m) : 
			print(a[i][n - 1], end = " ") 
			
		n -= 1
		# Print the last row from the remaining rows 
		if ( k < m) : 
			
			for i in range(n - 1, (l - 1), -1) : 
				print(a[m - 1][i], end = " ") 
			
			m -= 1
		# Print the first column from the remaining columns 
		if (l < n) : 
			for i in range(m - 1, k - 1, -1) : 
				print(a[i][l], end = " ") 
			
			l += 1
row,col=[int(i) for i in input().split()]
a=[[int(input()) for i in range(col)]for j in range(row)]
spiralPrint(row, col, a) 
