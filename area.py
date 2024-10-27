a=int(input("Enter the side of triangle:"))
b=int(input("Enter the side of triangle:"))
c=int(input("Enter the side of triangle:"))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("Area of triangle is:",area)
print("Semi perimeter of the triangle is:",s)
