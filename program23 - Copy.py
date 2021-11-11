#Fibonacci series upto n
n=int(input())
i=0
j=1
while n>0:
    print(i,end=' ')
    i,j=j,i+j
    n-=1
    
    
