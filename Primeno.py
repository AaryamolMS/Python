lower_limit=int(input("Enter lower limit: "))
upper_limit=int(input("Enter upper limit: "))
for i in range(lower_limit,upper_limit):
    if i>1:
        for j in range(2,i):
            if(i%j==0):
                break;
else:
    print(i)    