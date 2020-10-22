def a_shape(rows):
	k=rows
	s=0
	print("\n Ashape \n")
	for rows in range(rows):
		for star in range(k):
			print("*", end=' ')
		for space in range(s):
			print(' ', end=' ')	
		for star in range(k):	
			print("*", end=' ')
		k=k-1
		s=s+2
		print()	



def main():
	rows=int(input("Enter no. of rows: "))
	a_shape(rows)
if __name__=='__main__':
	main()