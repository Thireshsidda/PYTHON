#Twin prime pair:- A prime pair is called Twin prime pair if the difference between
#                  two primes in that pair is only 2.
#                  Ex:-3,5

def is_prime(n):
    if n==1:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
        return True
a,b=map(int,input().split())
for i in range(a,b+1):
    if is_prime(i) and is_prime(i+2):
        print(i,i+2)
    
        
