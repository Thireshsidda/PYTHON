#print all odd numbers in a given range a=1 to b=10.
a=int(input())
b=int(input())
while(a<=b):
    if(a%3!=0):
        print(a,end=' ')
    a+=1
        
