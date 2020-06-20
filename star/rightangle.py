class rightangle:
	def __init__(self,r):
		self.r=r
		#self.c=c
	def left(self):
		print("\n Descending rightangle pyramid")
		for row in range(self.r+1):
			for col in range(row):
				print("*",end=' ')
			print()	
	def right(self):
		print("\n Ascending rightangle pyramid \n")
		k=self.r
		i=1
		for row in range(self.r+1):
			for space in range(k):
				print(" ", end=' ')
			for col in range(i):
				print("*", end=' ')	
			k=k-1
			i=i+1		
			print()	
	def vshape(self):
		rows=self.r
		k=(2*rows)-2
		i=1
		print("\n vshape \n")
		for row in range(rows):
			for star in range(i):
				print('*', end=' ')
			for space in range(k):
				print(' ', end=' ')	
			for star in range(i):
				print("*", end=' ')
			print()
			i=i+1
			k=k-2		

	def ashape(self):
		rows=self.r
		k=rows
		s=0
		print("\n Ashape \n")
		for rows in range(self.r):
			for star in range(k):
				print("*", end=' ')
			for space in range(s):
				print(' ', end=' ')	
			for star in range(k):	
				print("*", end=' ')
			k=k-1
			s=s+2
			print()
	def kite(self):
		print("\n kite \n")	
		rows=self.r
		k=rows
		s=0
		for rows in range(self.r):
			for star in range(k):
				print("*", end=' ')
			for space in range(s):
				print(' ', end=' ')	
			for star in range(k):	
				print("*", end=' ')
			k=k-1
			s=s+2
			print()

		l=(2*rows)
		i=1
		for row in range(self.r):
			for star in range(i):
				print('*', end=' ')
			for space in range(l):
				print(' ', end=' ')
			for star in range(i):
				print("*", end=' ')
			i=i+1
			l=l-2
			print()
			
				
				

				
x=int(input("Enter rows: "))
#y=int(input("Enter cols: "))
p=rightangle(x)
p.left()	
p.right()
p.vshape()
p.ashape()
p.kite()