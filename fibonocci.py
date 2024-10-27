def fibonocci(n):
    if n==0 or n==1:
               return n
    else:
	        return fibonocci(n-1)+fibonocci(n-2)
n=int(input("Enter the number of terms:"))
print("The fibonacci series is...")
for i in range(n):
	       print(fibonocci(i))
result=fibonocci(n-1)
