#Prime numbers in a given range using functions
def is_prime(n):
    if n==1:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
a,b=map(int,input().split())
for i in range(a,b+1):
    if is_prime(i):
        print(i,sep='/n')
