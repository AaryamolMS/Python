lowerlimit=int(input("Enter lower limit:"))
upperlimit=int(input("Enter upper limit:"))
for i in range(lowerlimit,upperlimit+1):
	if i>1:
		for j in range(2,i):
			if(i%j==0):
				break;
		else:
		 	print(i)
