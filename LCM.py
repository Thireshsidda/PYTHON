a,b=map(int,input().split())
if a>b:
    a,b=b,a
c=b
while b%a!=0:
    b+=c
print(b)
    
        
        
        
