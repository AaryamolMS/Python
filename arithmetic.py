num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
print("Enter the choice you want:\n1.Addition \n2.Subtraction \n3.Multilpication \n4.Division \n5.Exponent \n6.floor division \n7.Modules")
choice=int(input("Enter the choice you want"))
if choice==1:
	print("Sum is:",num1+num2)
elif choice==2:
	print("Difference is:",num1-num2)
elif choice==3:
	print("Multiplication is:",num1*num2)
elif choice==4:
	print("Division is:",num1/num2)
elif choice==5:
	print("Exponent is:",num1**num2)
elif choice==6:
	print("Floor division is:",num1//num2)
elif choice==7:
	print("Modules is:",num1%num2)
else :
	print("Invalid choice")	
