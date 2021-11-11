#Fibonacci upto n
n=int(input())
i=0
j=1
if n==1:
    print(i,end=' ')
else:
    print(i,j,end=' ')
    while n>2:
        k=i+j
        print(k,end=' ')
        i,j=j,k
        n-=1
