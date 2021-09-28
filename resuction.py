
a=[]
l=int(input("Enter lower limit: "))
u=int(input("Enter upper limit: "))
a=[x for x in range(l,u+1) if x%2!=0 and str(x)==str(x)[::-1]]
print("The numbers are: ",a)	
	