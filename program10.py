a=int(input('Enter customer ID:'))
b=int(input('Enter units consumed:'))
if b<=199:
    n=b*1.2
elif 200<=b>=400:
    n=b*1.5
elif 400<=b>=600:
    n=b*1.8
else:
    n=b*2
if n>400:
    s=0.15*n
else:
    s=0
total=s+n
print('Enter customer id:',a)
print('Enter units cosumed:',b)
print('Current bill:',n)
print('Subcharge:',s)
print("Total:",total)
    
