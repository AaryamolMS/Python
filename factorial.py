def recur_factorial(n):
   if n ==0 or n==1:
       return n
   else:
       result=recur_factorial(n-1)
       return n*result

num=int(input("Enter a number:"))
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
	print("The factorial of", num, "is", recur_factorial(num))

