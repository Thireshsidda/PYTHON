#To find given number is perfect or not
#condition for perfect number--->Sum of proper factors of a given number is equal to that given number.
n=int(input("Enter a number"))
s=0
for i in range(1,n//2+1):
    if i%2==0:
        s+=i
if s==n:
    print(n,"is a perfect number")
else:
    print(n,"is not a perfect number")
