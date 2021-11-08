#sum of Even fibonacci series below four million
n=0
i=1
j=2
k=i+j
while i<=4000000:
    i,j=j,k
    k=i+j
    if i%2==0:
        n=n+i
print(n)
    
     
    
    
