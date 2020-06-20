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

def triangle(base):
	if base%2==0:
		d=base//2
		w=1
		print()
		for i in range(1,d):
			if i==1:
				print('*')
			for star in range(1):
				print('*', end=' ')
			for space in range(w):
				print(" ", end=' ')
				w=w+1
			for star in range(1):
				print('*', end=' ')
		
		for star in range(d):
			print("*")
		print()		


	


x=int(input("Enter rows: "))
square(x)
triangle(x)
