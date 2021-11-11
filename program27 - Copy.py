#sum of the digits  a number
n=int(input())
i=0
while n:
    r=n%10
    i+=r
    n=n//10
print(i)
