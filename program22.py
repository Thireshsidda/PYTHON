#fibonacci up to n
n=int(input('Enter a number'))
i=0
j=1
f=0
while i<=n:
    print(i)
    i,j=j,f
    f=i+j
     
    
    
