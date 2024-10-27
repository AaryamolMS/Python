num1=int(input("Enter the number for which multiplication table is to be generated: "))
end=int(input("Enter the limit: "))
for i in range(1,end+1):
    print(num1,"*",i,"=",num1*i)