a,b=0,1
n=int(input("enter range"))

if(n>2):
	print(a,b,end=" ")
	for i in range(2,n+1):
		a,b=b,a+b
		print(b,end=" ")
else:
	print(a,b)