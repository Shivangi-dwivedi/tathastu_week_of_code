n=int(input())

#to check even or odd
if(n%2==0):
	print("even")
else:
	print("odd")

# to check prime number
if(n>1):
	for i in range(2,n):
		if n%i==0:
			print("not prime")
			break
	else:
		 print("prime")
else:
	print("not prime")

# to check palindrome or not
t=n
rev=0
while (n!=0):
	r=n%10
	rev=(rev*10)+r
	n//=10
	if(rev==t):
	    print("palindrome")
	    break
else:
	print("not palindrome")

# to check Armstrong number
import math 
l=len(str(n))
t=n
sum=0
while(n!=0):
	 r=n%10
	 sum+=pow(r,l)
	 n=n//10
if (sum==t):
	print("no. is armstrong")
else:
	print("not an armstrong")
