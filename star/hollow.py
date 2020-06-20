def square(row):
	r=row
	c=row
	k=row-2
	for top in range(row):
		print("*", end=' ')
	print()
	for side in range(k):
		for star in range(1):
			print('*', end=' ')
		for space in range(k):
			print(' ', end=' ')
		for star in range(1):
			print('*', end=' ')
		print()	
	for top in range(row):
		print("*", end=' ')
	print()	


x=int(input("Enter rows: "))
square(x)
