#Fibonacci series upto n
n=int(input())
i=0
j=1

while n>0:
    i,j=j,i+j
print(i,end=' ')
n-=1
    
    
    
