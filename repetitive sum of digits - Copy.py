#Finding repetitive sum of digits
n=int(input())
while True:
    s=0
    while n: #24
        r=n%10 #9
        s+=r #24
        n=n//10 #0
    if s<10:#24<10
        break
    n=s#24
print(s)
