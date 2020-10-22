def descend(r):
	for col in range(r+1):
		for row in range(col):
			print("*",end="")
		print()

def main():
	rows=int(input("Enter rows:  "))
	descend(rows)
if __name__=='__main__':
	main()
