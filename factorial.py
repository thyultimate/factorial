# limit = 5
# factorial = 1
# for num in range(1,limit+1):
#    factorial*=num
# print factorial


# fact(5)=5*fact(4)
# fact(n)=n*fact(n-1)
# fact(1)=1

def fact(n):
	if n==1:
		return 1
	else :
		return n*fact(n-1) 

print fact(5)