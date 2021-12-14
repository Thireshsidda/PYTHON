#Megaprime:- A prime number is called a Mega prime if and only if all the digits of that number are also prime.

#Function to find if the number is prime or not.
def prime_num(n):
    if n==1:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
        return True

#Function to find if all the digits are prime or not.
def digits_prime(x):
    while x:
        r=x%10
        if not prime_num(r):
            return False
        x=x//10
    return True
    
#Function to find number is megaprime or not.
def mega_prime(a):
    if prime_num(a) and digits_prime(a):
        return True
    return False
a,b=map(int,input().split())
for i in range(a,b+1):
    if mega_prime(i):
        print(i)

