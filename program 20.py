a=int(input('From:'))
b=int(input('To:'))
while a<=b:
    print(a,'table multiples upto??')
    j=int(input())
    i=1
    while i<=j:
        print(a,'X',i,'=',a*i)
        i+=1
    print()
    a+=1
