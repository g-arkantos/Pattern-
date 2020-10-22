class matrix:
	def __init__(self,r,c):
		self.r=r
		self.c=c
	def pattern(self):
		for i in range(self.r):
			for j in range(self.c):
				print("*",end=' ')	
			print(" ")	
x=int(input("Enter rows: "))
y=int(input("Enter cols: "))
p=matrix(x,y)
p.pattern()	
