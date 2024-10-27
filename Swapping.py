#with another variable
a=10
b=20
temp=a
a=b
b=temp
print("A after swapping:",a)
print("B after swapping:",b)
print("-----------------------------------------------------------------------------------------------------------------------------------------")

#with out using a variable
num1=50
num2=70
print("num1 before swapping:",num1)
print("num2 before swapping:",num2)
num1=num1+num2 #120
num2=num1-num2 #50
num1=num1-num2
print("num1 after swapping:",num1)
print("num2 after swapping:",num2)
