def ascend(r):
	for col in range(r):
		for row in range(r-col):
			print("*", end="")
		print()
def main():
	rows=int(input("Enter rows:  "))
	ascend(rows)	
if __name__=='__main__':
	main()
