
def staircase(n):
    for i in range(n,0,-1):
        for j in range(1,n+1):
            if j>=i:
                print('#',end='')
            else:
                print(end=' ')
        print()

n = int(input())
staircase(n)
