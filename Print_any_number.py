limit=int(input("Enter the limit: "))
for i in range(1,limit+1):
    num=int(input("Enter a number").format(i))
    print("The number you entered is: ",num)
