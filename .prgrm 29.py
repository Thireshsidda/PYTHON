#To find factors of number
n=int(input("Enter a number"))
for i in range(1,n+1):
    if n%i==0:
        print(i)


#To decrease the iteration and complexity of a number
n=int(input("Enter a number"))
for i in range(1,n//2+1):
    if n%i==0:
        print(i)
print(n)
