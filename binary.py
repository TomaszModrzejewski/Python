
l=[]
def convert(b):
    if(b==0):
        return l
    dig=b%2
    l.append(dig)
    convert(b//2)
a=int(input("Enter a number: "))
convert(a)
l.reverse()
print("Binary equivalent:")
for i in l:
    print(i)	
	