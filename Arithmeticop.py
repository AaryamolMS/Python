num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
choice=int(input("\nEnter your choice you want:\n1.Addition \n2.Subtraction \n3.Multiplication \n4.Division \n5.Modules \n6.Floor\n"))
if choice==1:
    print("Sum is",num1+num2)
elif choice==2:
        print("Difference is:",num1-num2)
elif choice==3:
        print("Product is:",num1*num2)
elif choice==4:
        print("Division is:",num1/num2)
elif choice==5:
        print("Modules is:",num1%num2)
elif choice==6:
        print("Floor is:",num1//num2)
else:
    print("Invalid choice!!!!!")

