a=int(input("Enter first side of the triangle:"))
b=int(input("Enter second side of the triangle:"))
c=int(input("Enter second side of the triangle:"))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("Semi perimeter of the triangle is :",s)
print("Area of the triangle is :",area)